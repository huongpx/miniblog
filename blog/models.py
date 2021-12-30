from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Post(models.Model):
    """Model representing a blog"""
    title = models.CharField(max_length=100)

    content = models.TextField(max_length=1000)

    author = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)

    post_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-detail', args=str(self.id))

    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.title

class Member(models.Model):
    """Model representing a blog's author"""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    info = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('member-detail', args=str(self.id))
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User) 
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
    instance.member.save()


class PostComment(models.Model):
    """Model representing a comment in a blog"""
    content = models.TextField(max_length=500)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_time']


    def __str__(self):
        show_length = 80
        if len(self.content) > show_length:
            show_content = self.content[:show_length] + '...'
        else:
            show_content = self.content
        return show_content
