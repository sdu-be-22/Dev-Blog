import os
import posixpath
import random
from audioop import reverse

from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

from blog import settings


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.TextField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    views = models.ManyToManyField(Ip, related_name="post_views", verbose_name="Views", blank=True)

    class Meta:
        verbose_name_plural = "posts"

    def total_views(self):
        return self.views.count()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    @staticmethod
    def get_absolute_url():
        return reverse('home')


def user_directory_path(instance, filename):
    profile_pic_name = 'profiles/user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_pic_name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profession = models.TextField(null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    telegram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 300, 300
        if self.profile_pic:
            pic = Image.open(self.profile_pic.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.profile_pic.path)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Subscribed Users"

    def __str__(self):
        return self.name + ' ' + self.email
