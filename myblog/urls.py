from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/<slug:slug>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<slug:slug>', UpdatePostView.as_view(), name="update_post"),
    path('article/<slug:slug>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('posts/<str:author>/', MyPostsView, name="my_posts"),
    path('like/<slug:slug>/', LikeView, name="like_post"),
    path('liked/<str:user>/', UserLikedPostsView, name="liked_posts"),
    path('subscribe/', SubscribeNewsletterView.as_view(), name="subscribe_newsletter"),
    path('tag/<str:slug>', TagPosts, name="tag_posts"),
    # path('post-json/<int:num_posts>', PostsJsonView.as_view(), name="post-json-view"),
]
