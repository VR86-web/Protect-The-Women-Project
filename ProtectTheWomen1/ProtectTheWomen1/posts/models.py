from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Post(models.Model):

    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class Like(models.Model):
    to_post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
