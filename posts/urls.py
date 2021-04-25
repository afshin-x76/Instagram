from django.urls import path
from .views import PostListView, PostDetailView, EditPostView, CreatePostView
app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post-edit/<int:pk>', EditPostView.as_view(), name='post_edit'),


]