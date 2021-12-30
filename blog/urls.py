from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
]