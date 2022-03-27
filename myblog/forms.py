from django import forms
from .models import Post, Category, Comment, SubscribedUsers


# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'header_image', 'body', 'snippet')

        choices = Category.objects.all().values_list('name', 'name')
        choice_list = []

        for item in choices:
            choice_list.append(item)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author_id', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'richtext_field'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'snippet', 'body')

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