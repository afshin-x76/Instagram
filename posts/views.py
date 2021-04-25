from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post, Tag
from django.views.generic.edit import UpdateView
from .forms import CreatePostForm, CreateCommentForm


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context

    def get_queryset(self):
        tag = self.request.GET.get('q')
        if tag:
            queryset = Post.objects.filter(tag=tag)
            return queryset
        else:
            return Post.objects.all()


# class NewListView(View):
#     def get(self,request,pk=None):
#         if 


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-detail.html'
    context_object_name = 'post'


class EditPostView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CreatePostForm(instance=post)
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'posts/post-edit-or-add.html', context=context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:post_list'))
        return httpResponse("Not valid")


class CreatePostView(View):
    pass

    