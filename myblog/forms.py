from datetime import datetime

from django import forms
from taggit.models import Tag
from django.forms.models import model_to_dict

from .models import Post, Category, Comment, SubscribedUsers

choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'tags', 'header_image', 'body', 'snippet', 'publish')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'type': 'hidden'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author_id', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'richtext_field'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'tags', 'snippet', 'body')
        # choices = []
        # for tag in Tag.objects.all():
        #     choices.append(tag.name)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'richtext_field'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class SubscribeUserForm(forms.ModelForm):
    class Meta:
        model = SubscribedUsers
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body', 'user')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
