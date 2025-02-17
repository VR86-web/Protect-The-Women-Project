from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

        labels = {
            "username": "",
            "email": "",
            "password1": "",
            "password2": "",
        }
        help_texts = {
            "Please enter your username...": "",
            "Please enter your email...": "",
        }

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username:"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email:"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control",
                "placeholder": "Password: (at least 8 characters long)"}),

            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password:"}),
        }

        error_messages = {
            "username": {
                "required": "Username is required. Write it!",
                "unique": "This username is already taken.",
            },
            "email": {
                "required": "Email is required. Write it!",
                "unique": "This email is already taken.",
            },
            "password1": {
                "required": "Password is required. Write it!",
                "min_length": "Password must be at least 8 characters long.",
                "invalid": "Password must contain at least one uppercase letter, one lowercase letter,"
                           " one number, and one special character.",
            },
        }
