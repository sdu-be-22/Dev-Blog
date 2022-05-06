from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import PostSerializer, PostDetailSerializer, CommentSerializer
from myblog.models import Category, Post, Profile, Comment


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List': '/post-list/',
        'Detail View': '/post-detail/<str:pk>/',
        # 'Create': '/post-create/',
        # 'Update': '/post-update/<str:pk>/',
        # 'Delete': '/post-delete/<str:pk>/',
    }

    return Response(api_urls)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs['slug']
        articles = Post.objects.filter(slug=slug)
        return articles


# class CommentDetailAPIView(RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# @api_view(['GET'])
# # @permission_classes((permissions.AllowAny,))
# def CommentDetailAPIView(request, pk):
#     post = Comment.objects.filter(post=pk)
#     serializer = CommentSerializer(post, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def postList(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True, context={'posts': posts})
#     return Response(serializer.data)
#
#
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)
#
#
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def postCreate(request):
#     serializer = PostDetailSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
