from django.shortcuts import render, redirect
from .forms import AccountCreationForm
from account.models import Account
from django.db import IntegrityError
from django.contrib.auth import authenticate , login
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# used for register page
def register(response):
    args = {}
    try:
        if response.method == "POST":
            form = AccountCreationForm(response.POST)
            if form.is_valid():
                user = form.save()
    
                account = Account(email=user.email, user=user, firstName=user.first_name, lastName=user.last_name)
                account.save()
                
                login(response,user)
                return redirect('loginRedirect')
                # after logging in add redirect page here
        else:
            form = AccountCreationForm()
        args['form'] = form
            
    except IntegrityError as e:
        return render(response, 'account/registered.html', {"message":e.message})


    form = RegisterForm()
    return render(response, 'account/registered.html', {"form": form})
