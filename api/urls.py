from django.urls import path
from api.views import apiOverview, \
    PostListAPIView, \
    PostDetailAPIView
from members.views import ShowProfilePageView
from . import views

urlpatterns = [
    path('', apiOverview, name="apihome"),
    # path('post-list/', views.postList, name="postList"),
    # path('post-create/', views.postCreate, name="postCreate"),
    # path('post-detail/<str:pk>/', views.postDetail, name="postDetail"),

    path('post-list/', PostListAPIView.as_view(), name="list"),
    path('post-detail/<slug:slug>', PostDetailAPIView.as_view(), name="detail"),
    # path('comment-detail/<str:pk>', CommentDetailAPIView, name="comment-detail"),
    # path('<str:author>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
]
