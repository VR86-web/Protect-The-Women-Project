from django.contrib.auth import get_user_model
from django.db import models

from ProtectTheWomen.posts.models import Posts


UserModel = get_user_model()


class Comments(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]

        ordering = ['-created_at']

    to_post = models.ForeignKey(
        to=Posts,
        on_delete=models.CASCADE,
    )

    content = models.TextField()

    created_at = models.DateTimeField()

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,

    )


class Likes(models.Model):
    to_post = models.ForeignKey(
        to=Posts,
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,

    )
