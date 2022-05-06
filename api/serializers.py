from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers
from myblog.models import Category, Post, Profile, Comment
from ckeditor.fields import RichTextField


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'user',
            'name',
            'body',
            'date_added',
        ]

    def get_name(self, obj):
        name = obj.user.first_name + " " + obj.user.last_name
        return name


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='detail', lookup_field='slug')
    # author_profile_url = serializers.HyperlinkedIdentityField(view_name='show_profile_page', lookup_field='author')
    author = serializers.ReadOnlyField(source='author.id')
    header_image = serializers.SerializerMethodField()
    author_profile_image = serializers.SerializerMethodField()
    post_date = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = (
            'url',
            # 'author_profile_url',
            'author_profile_image',
            'id',
            'title',
            'title_tag',
            'author',
            'header_image',
            'post_date',
            'category',
            'body',
            'snippet',
        )

    def get_author_profile_image(self, obj):
        try:
            author_profile_image = obj.author.profile.profile_pic.url
        except:
            author_profile_image = None
        return author_profile_image

    def get_author(self, obj):
        return str(obj.author.id) + '|' + obj.author.username + '|' + obj.author.first_name + ' ' + obj.author.last_name

    def get_header_image(self, obj):
        try:
            header_image = obj.header_image.url
        except:
            header_image = None
        return header_image


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    header_image = serializers.SerializerMethodField()
    author_profile_image = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    post_date = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = (
            'author_profile_image',
            'id',
            'title',
            'title_tag',
            'author',
            'header_image',
            'post_date',
            'category',
            'body',
            'snippet',
            'likes',
            'comments',
        )

    def get_comments(self, obj):
        data = CommentSerializer(Comment.objects.filter(post=obj.id), many=True)
        return data.data

    def get_author(self, obj):
        return str(obj.author.id) + '|' + obj.author.username + '|' + obj.author.first_name + ' ' + obj.author.last_name

    def get_header_image(self, obj):
        try:
            header_image = obj.header_image.url
        except:
            header_image = None
        return header_image

    def get_author_profile_image(self, obj):
        try:
            author_profile_image = obj.author.profile.profile_pic.url
        except:
            author_profile_image = None
        return author_profile_image

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['author'] = instance.first_name + instance.last_name
    #     return response

    # def to_representation(self, instance):
    #     owner = Post.author.first_name + " " + Post.author.last_name
    #     return owner

    def get_image_url(self, obj):
        return obj.header_image.url
