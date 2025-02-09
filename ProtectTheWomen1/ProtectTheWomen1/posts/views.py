from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from ProtectTheWomen1.posts.forms import PostCreateForm
from ProtectTheWomen1.posts.models import Post


# Create your views here.


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('index')


class AllPostView(ListView):
    model = Post
    template_name = 'posts/all-post.html'


class UpdatePostView(UpdateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'posts/update-post.html'
    success_url = reverse_lazy('all-posts')

