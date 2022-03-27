from django.urls import path
from .views import AddPostView, \
    HomeView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, \
    AddCommentView, MyPostsView, UserLikedPostsView, SubscribeNewsletterView, PostsJsonView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('posts/<str:author>/', MyPostsView, name="my_posts"),
    path('like/<int:pk>/', LikeView, name="like_post"),
    path('liked/<str:user>/', UserLikedPostsView, name="liked_posts"),
    path('subscribe/', SubscribeNewsletterView.as_view(), name="subscribe_newsletter"),
    # path('post-json/<int:num_posts>', PostsJsonView.as_view(), name="post-json-view"),
]
