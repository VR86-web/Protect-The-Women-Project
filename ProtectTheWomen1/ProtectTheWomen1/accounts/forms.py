from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ProtectTheWomen1.accounts.models import Profile

UserModel = get_user_model()


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email", "password1", "password2")

        labels = {
            "username": "",
            "email": "",
            "password1": "",
            "password2": "",
        }

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username:"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email:"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password: (at least 8 characters long)"}),

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


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = ("username", "email")


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass


class ProfileCreateForm(ProfileBaseForm):
    pass
