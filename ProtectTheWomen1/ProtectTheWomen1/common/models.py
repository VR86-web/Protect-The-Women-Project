from cloudinary.models import CloudinaryField
from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=200,
    )
    content = models.TextField()

    image = CloudinaryField(
        'profile_picture',
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


