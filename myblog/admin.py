from django.contrib import admin
from .models import Post, Category, Profile, Comment, SubscribedUsers, Ip


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(SubscribedUsers)
admin.site.register(Ip)
