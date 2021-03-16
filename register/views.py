from django.shortcuts import render, redirect
from .forms import RegisterForm
from myapp.models import Account
from django.contrib.auth import authenticate

# Create your views here.

# used for register page


def register(response):
    context = {}
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data('password1')
            first_name = form.cleaned_data('first_name')
            last_name = form.cleaned_data('last_name')
            username = form.cleaned_data('username')
            account = authenticate(email=email, password=raw_password,
                                   first_name=first_name, last_name=last_name, username=username)

    # after loging in add redirect page here

        else:
            print("not valid")
    else:
        form = RegisterForm()
        context['registration_form'] = form

    form = RegisterForm()
    return render(response, 'registered.html', {"form": form})
