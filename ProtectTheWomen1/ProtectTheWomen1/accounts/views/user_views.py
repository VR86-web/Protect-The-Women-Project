from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ProtectTheWomen1.accounts.forms import CustomUserForm

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        profile = self.request.user.profile

        if not profile.first_name and not profile.last_name and not profile.date_of_birth and not profile.country:
            return reverse_lazy('profile-create')

        return reverse_lazy('profile-details', kwargs={'pk': profile.pk})


class UserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserForm
    template_name = 'accounts/registration-template.html'
    success_url = reverse_lazy('login')