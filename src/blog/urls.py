from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('post/create/', views.PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/comment/', views.PostCommentCreate.as_view(), name='post-comment'),
    path('myposts/', views.MyPostListView.as_view(), name='my-post'),
]