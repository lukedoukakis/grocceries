from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django import forms

from account.models import Account

class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True, widget=forms.TextInput(attrs={'placeholder':"Email"}))
    phone = PhoneNumberField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    agree_tos = forms.BooleanField(label='I agree to the terms and conditions')

    class Meta:
        model = Account
        fields = ("username", "email", "first_name",
                           "last_name", "phone", "password1", "password2", "agree_tos")
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Field('email'),
            Field('first_name'),
            Field('last_name'),
            Field('phone'),
            Field('password1'),
            Field('password2'),
            'agree_tos',
            Submit('submit', 'Register') 
        )


