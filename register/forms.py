from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.Field()
    last_name = forms.Field()

    class Meta:
        model = User
        fields = ["email", "username", "first_name",
                  "last_name", "password1", "password2", ]
