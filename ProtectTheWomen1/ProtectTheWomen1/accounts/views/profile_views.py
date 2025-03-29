from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from ProtectTheWomen1.accounts.forms import ProfileEditForm, ProfileDeleteForm, ProfileCreateForm
from ProtectTheWomen1.accounts.models import Profile

UserModel = get_user_model()


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-template.html'

    class ProfileDetailsView(LoginRequiredMixin, DetailView):
        model = Profile
        template_name = 'accounts/profile-template.html'

        def get_object(self, queryset=None):
            profile = get_object_or_404(Profile, user=self.request.user)

            if not profile.first_name and not profile.last_name and not profile.date_of_birth and not profile.country:
                return redirect('profile-create')

            return profile


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


class ProfileCreateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'accounts/profile-create-template.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.profile.pk})