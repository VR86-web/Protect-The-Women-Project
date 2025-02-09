from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from ProtectTheWomen.common.forms import CommentForm
from ProtectTheWomen.posts.forms import PostCreateForm, PostDeleteForm, PostUpdateForm
from ProtectTheWomen.posts.models import Posts


# Create your views here.


def posts_list(request):
    posts = Posts.objects.all()

    posts_per_page = 5

    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'posts/posts-list.html', context)


class AddPost(CreateView):
    model = Posts
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('posts-list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user

        return super().form_valid(form)


class DetailsPost(LoginRequiredMixin, DetailView):
    model = Posts
    template_name = 'posts/single-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm

        return context


class DeletePost(DeleteView):
    model = Posts
    template_name = 'posts/delete-post.html'
    form_class = PostDeleteForm
    success_url = reverse_lazy('posts-list')

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.initial()
        })

        return kwargs


class UpdatePost(UpdateView):
    model = Posts
    form_class = PostUpdateForm
    template_name = 'posts/update-post.html'
    success_url = reverse_lazy('posts-list')


