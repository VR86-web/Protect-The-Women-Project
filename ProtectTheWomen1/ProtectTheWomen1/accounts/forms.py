from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.widgets import CountrySelectWidget

from ProtectTheWomen1.accounts.models import Profile

UserModel = get_user_model()


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email:"}),
        error_messages={"required": "Email is required. Write it!", "unique": "This email is already taken."},
    )

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email", "password1", "password2")


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
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass


class ProfileCreateForm(ProfileBaseForm):
    pass
