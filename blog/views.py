from django.shortcuts import render
from .models import Post, Member, PostComment
from django.views import generic

# Create your views here.

def about(request):
    """View function for index page"""
    num_posts = Post.objects.count()
    
    num_members = Member.objects.count()

    num_comments = PostComment.objects.count()

    context = {
        'num_posts': num_posts,
        'num_members' : num_members,
        'num_comments': num_comments,
    }

    return render(request, 'about.html', context=context)


class MemberListView(generic.ListView):
    """Class base view for blogger list"""
    model = Member
    paginate_by = 5


class MemberDetailView(generic.DetailView):
    model = Member


class PostListView(generic.ListView):
    """Class base view for blog list"""
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
