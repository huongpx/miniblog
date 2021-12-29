from django.shortcuts import render
from .models import Blog, Blogger, BlogComment
from django.views import generic

# Create your views here.

def about(request):
    """View function for index page"""
    num_blogs = Blog.objects.count()
    
    num_bloggers = Blogger.objects.count()

    num_comments = BlogComment.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_comments': num_comments,
    }

    return render(request, 'about.html', context=context)


class BloggerListView(generic.ListView):
    """Class base view for blogger list"""
    model = Blogger
    paginate_by = 5


class BloggerDetailView(generic.DetailView):
    model = Blogger


class BlogListView(generic.ListView):
    """Class base view for blog list"""
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog
