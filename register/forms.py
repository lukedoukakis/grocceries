from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from account.models import Account


class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True)
    phone = PhoneNumberField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Account
        fields = ("username", "email", "first_name",
                           "last_name", "phone", "password1", "password2",)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
