from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from ProtectTheWomen.ProtectTheWomen.accounts.forms import AppUserCreationForm, ProfileEditForm
from ProtectTheWomen.ProtectTheWomen.accounts.models import Profile

UserModel = get_user_model()


class UserLogin(LoginView):
    template_name = 'accounts/login.html'


class UserRegister(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.request.user.pk}
        )


def profile_delete_page(request, pk: int):
    return render(request, 'accounts/profile-delete.html')


def profile_details_page(request, pk: int):
    return render(request, 'accounts/profile.html')


class ProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})