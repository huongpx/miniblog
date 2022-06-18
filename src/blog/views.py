from django.shortcuts import render
from .models import Post, Member, PostComment
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

def about(request):
    """View function for About page"""
    # Number of total posts, members, comment in website
    num_posts = Post.objects.count()
    
    num_members = Member.objects.count()

    num_comments = PostComment.objects.count()

    # Context for template of About site
    context = {
        'num_posts': num_posts,
        'num_members' : num_members,
        'num_comments': num_comments,
    }

    return render(request, 'about.html', context=context)


class MemberListView(generic.ListView):
    """Generic class-base view for member list"""
    model = Member
    paginate_by = 5


class MemberDetailView(generic.DetailView):
    """Generic class-base detail view for a member"""
    model = Member


class PostListView(generic.ListView):
    """Generic class-base view for blog list"""
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    """Generic class-base detail view for a post"""
    model = Post


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(generic.CreateView):
    """Generic class-base create view for signing-up an user"""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


from django.views.generic.edit import CreateView

class PostCreate(CreateView):
    """Generic class-base create view for posting"""
    model = Post
    fields = ['title', 'content',]
    
    def form_valid(self, form):
        """Add author and associated post to form data before set as valid (so it is saved to model)"""
        form.instance.author = self.request.user
        # Call super-class form validation behaviour
        return super(PostCreate, self).form_valid(form)


class PostCommentCreate(CreateView):
    """Generic class-base create view for posting a comment"""
    model = PostComment
    fields = ['content',]

    def get_context_data(self, **kwargs):
        """Add asscociated post to form template"""
        context = super(PostCommentCreate, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        """Add author and associated post to form data before set as valid (so it is saved to model)"""
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(PostCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """After posting comment return to associated post"""
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})

from django.contrib.auth.mixins import LoginRequiredMixin

class MyPostListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view for a list of post of logged in user"""
    model = Post
    template_name = 'blog/my_post_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        """Filter the post by the logged in user"""
        return Post.objects.filter(author=self.request.user).order_by('-post_time')
