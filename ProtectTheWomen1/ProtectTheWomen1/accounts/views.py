from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from ProtectTheWomen1.accounts.forms import CustomUserForm, ProfileEditForm, ProfileDeleteForm, ProfileCreateForm
from ProtectTheWomen1.accounts.models import Profile

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class UserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserForm
    template_name = 'accounts/registration-template.html'
    success_url = reverse_lazy('login')


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile_template.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-template.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-template.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('login')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Profile.objects.get(pk=pk)
        return post.__dict__

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'accounts/profile-create-template.html'
    success_url = reverse_lazy('profile-details')

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()
