from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from account.models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email", "username", "first_name",
                           "last_name", "password1", "password2",)

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        # Check to see if any users already exist with this email as a username.
        try:
            match = Account.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email
        
        # A user was found with this as a email address, raise an error.
        raise forms.ValidationError(self.error_messages['email_exists'], code='email_exists')

    def save(self, commit=True):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data)


   