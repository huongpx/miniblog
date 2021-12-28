from django.contrib import admin
from .models import Blog, Blogger, BlogComment
# Register your models here.

admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(BlogComment)
