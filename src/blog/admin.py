from django.contrib import admin
from .models import Post, PostComment, Member
# Register your models here.

admin.site.register(Post)
admin.site.register(Member)
admin.site.register(PostComment)
