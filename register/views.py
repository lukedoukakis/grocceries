from django.shortcuts import render, redirect
from .forms import RegisterForm
from account.models import Account
from django.db import IntegrityError
from django.contrib.auth import authenticate , login


# used for register page
def register(response):
    try:
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                user = form.save()
                account = Account(
                    email=user.email, user=user, firstName=user.first_name, lastName=user.last_name)
                account.save()
                login(response,user)
                return render(response, 'myapp/landingPage.html')
            # after logging in add redirect page here

    except IntegrityError:
        #add error message your username/email/phone is already taken use a different one please
        return render(response, 'myapp/landingPage.html')


    form = RegisterForm()
    return render(response, 'account/registered.html', {"form": form})
