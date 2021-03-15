from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.

# used for register page


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    # after loging in add redirect page here

        else:
            print("not valid")

    form = RegisterForm()
    return render(response, 'registered.html', {"form": form})
