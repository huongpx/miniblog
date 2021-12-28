from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    """Model representing a blog"""
    title = models.CharField(max_length=100)

    content = models.TextField(max_length=1000)

    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blogger(models.Model):
    """Model representing a blog's author"""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    info = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username


class BlogComment(models.Model):
    """Model representing a comment in a blog"""
    content = models.TextField(max_length=500)

    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        show_length = 80
        if self.content > show_length:
            show_content = self.content[:show_length] + '...'
        else:
            show_content = self.content
        return show_content
