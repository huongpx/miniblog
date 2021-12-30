from django.shortcuts import render
from .models import Post, Member, PostComment
from django.views import generic
from django.urls import reverse

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


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


from django.views.generic.edit import CreateView

class PostCreate(CreateView):
    model = Post
    # Need to modify
    fields = '__all__'


class PostCommentCreate(CreateView):
    model = PostComment
    # Need to modify
    fields = '__all__'

    # Need to modify
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})

from django.contrib.auth.mixins import LoginRequiredMixin

class MyPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/my_post_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(author__user=self.request.user).order_by('-post_time')
