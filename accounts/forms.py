from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'last_name']

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)