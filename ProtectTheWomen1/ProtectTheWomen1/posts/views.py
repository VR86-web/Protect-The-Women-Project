from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from ProtectTheWomen1.posts.forms import PostCreateForm, PostDeleteForm, CommentForm
from ProtectTheWomen1.posts.models import Post


# Create your views here.


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('index')


class AllPostView(ListView):
    model = Post
    template_name = 'posts/all-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class UpdatePostView(UpdateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'posts/update-post.html'
    success_url = reverse_lazy('all-posts')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    form_class = PostDeleteForm
    success_url = reverse_lazy('all-posts')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


class CommentCreateView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('all-posts')

        return render(request, 'posts/all-post.html', {'post': post, 'form': form})

