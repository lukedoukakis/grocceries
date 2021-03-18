from django.shortcuts import render, redirect
from .forms import RegisterForm
from account.models import Account

from django.contrib.auth import authenticate


# used for register page
def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            account = Account(
                email=user.email, user=user, firstName=user.first_name, lastName=user.last_name)
            account.save()

        # after logging in add redirect page here
        else:
            print("not valid")

    form = RegisterForm()
    return render(response, 'account/registered.html', {"form": form})
