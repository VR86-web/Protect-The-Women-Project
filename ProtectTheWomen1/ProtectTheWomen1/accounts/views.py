from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ProtectTheWomen1.accounts.forms import CustomUserForm


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/registration-template.html'
    success_url = reverse_lazy('index')
