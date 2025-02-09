from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


class Posts(models.Model):
    title = models.CharField(max_length=255)

    content = models.TextField()

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,

    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
