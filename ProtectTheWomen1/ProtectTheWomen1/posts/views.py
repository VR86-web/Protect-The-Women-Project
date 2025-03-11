from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from ProtectTheWomen1.posts.forms import PostCreateForm, PostDeleteForm, CommentForm
from ProtectTheWomen1.posts.models import Post, Like, Comment


# Create your views here.


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('all-posts')


class AllPostView(ListView):
    model = Post
    template_name = 'posts/all-post.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'posts/update-post.html'
    success_url = reverse_lazy('all-posts')

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user == post.user


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    form_class = PostDeleteForm
    success_url = reverse_lazy('all-posts')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user == post.user


class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/detail-post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['is_creator'] = self.request.user == post.user
        context['form'] = CommentForm()
        context['comments'] = post.comments.all().order_by('-created_at')
        return context


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user

            comment.save()
            return redirect('all-posts')

        return render(request, 'posts/all-post.html', {'post': post, 'form': form})


@login_required
def reply_to_comment(request, pk, comment_id):
    post = get_object_or_404(Post, pk=pk)
    parent_comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                user=request.user,
                post=post,
                content=content,
                parent=parent_comment
            )
        return redirect('post-detail', pk=post.pk)

    return redirect('all-posts')


@login_required
def likes_functionality(request, pk: int):
    liked_object = Like.objects.filter(
        to_post_id=pk,
        user=request.user
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_post_id=pk, user=request.user)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{pk}')
