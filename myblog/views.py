import operator
import posixpath
from urllib.parse import urljoin

from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView, View

from blog.settings import BASE_DIR
from .models import Post, Category, Comment, SubscribedUsers, Profile, Ip
from .forms import PostForm, EditForm, AddCategoryForm, CommentForm, SubscribeUserForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse


# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})


def MyPostsView(request, author):
    my_posts = Post.objects.filter(author=author).order_by('-id')
    print(type(my_posts))
    return render(request, 'my_posts.html',
                  {'my_posts': my_posts})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats).order_by('-id')
    return render(request, 'category_posts.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        most_liked_post = Post.objects.annotate(total_likes=Count('likes')).order_by('-total_likes')[0:3]
        excl = []
        for ids in most_liked_post:
            excl.append(ids.id)
        posts = Post.objects.exclude(id__in=excl).order_by('-post_date')
        cat_menu = Category.objects.all()
        posts_count = Post.objects.count()
        list_of_users_and_likes = {}
        for i in User.objects.all():
            user_posts = Post.objects.filter(author=i.id)
            likes = 0
            for p in user_posts:
                likes += p.total_likes()
            list_of_users_and_likes[str(i.username)] = str(likes)
        # fin_max = max(list_of_users_and_likes, key=list_of_users_and_likes.get)
        sorted_d = dict(sorted(list_of_users_and_likes.items(), key=operator.itemgetter(1), reverse=True))
        max_user_likes = ""
        iterator = 0
        for i in sorted_d:
            if (iterator == 5):
                break
            max_user_likes += str(i) + ':' + sorted_d.get(i) + ';'
            iterator += 1
        users = User.objects.all()
        context["cat_menu"] = cat_menu
        context["most_liked_post"] = most_liked_post
        context["user_likes"] = max_user_likes
        context["users"] = users
        context["posts"] = posts
        context["posts_count"] = posts_count
        return context


def get_client_ip(request):
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forward_for:
        return x_forward_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            stuff.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            stuff.views.add(Ip.objects.get(ip=ip))

        total_likes = stuff.total_likes()
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


# def AddCommentView(request, pk):
#     if request.method == "POST":
#         # post = get_object_or_404(Post, id=request.POST.get('post_id'))
#         if request.POST.get('body'):
#             saveb = Comment()
#             saveb.body = request.POST.get('body')
#             saveb.save()
#         if request.POST.get('name'):
#             saven = Comment()
#             saven.name = request.POST.get('name')
#             saven.save()
#     return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
#


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         # post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #         if request.POST.get('body'):
    #             saveb = Comment()
    #             saveb.body = request.POST.get('body')
    #             saveb.save()
    #         if request.POST.get('name'):
    #             saven = Comment()
    #             saven.name = request.POST.get('name')
    #             saven.save()

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': str(self.kwargs['pk'])})


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        return super().form_valid(form)


class SubscribeNewsletterView(CreateView):
    model = Category
    form_class = SubscribeUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def UserLikedPostsView(request, user):
    global liked_posts
    if Post.objects.filter(likes=user).exists():
        liked_posts = Post.objects.filter(likes=user)
    else:
        liked_posts = None
    return render(request, 'user_liked_posts.html', {'liked_posts': liked_posts})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class PostsJsonView(View):

    def get(self, *args, **kwargs):
        upper = kwargs.get("num_posts")
        lower = upper - 3
        posts = list(Post.objects.values()[lower:upper])
        return JsonResponse({'data': posts}, safe=False)
