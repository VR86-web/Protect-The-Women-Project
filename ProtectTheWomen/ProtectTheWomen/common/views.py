from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ProtectTheWomen.common.forms import CommentForm
from ProtectTheWomen.common.models import Likes
from ProtectTheWomen.posts.models import Posts


# Create your views here.


def index(request):
    return render(request, 'common/index.html', )


def comment_functionality(request, post_id: int):
    if request.POST:
        post = Posts.objects.get(pk=post_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_post = post
            comment.author = request.user
            comment.save()

            return redirect('single-post', pk=post_id)


def likes_functionality(request, post_id: int):
    liked_object = Likes.objects.filter(
        to_post_id=post_id
    ).first()

    if liked_object:
        liked_object.delete()

    else:
        like = Likes(to_post_id=post_id, author=request.user)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{post_id}')


