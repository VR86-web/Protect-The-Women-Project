from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        auto_now=True,
        blank=True,
        null=True,
    )

    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name or 'Anonymous'

    def get_absolute_url(self):
        return reverse('profile-details', kwargs={'pk': self.pk})
