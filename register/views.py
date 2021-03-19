from django.shortcuts import render, redirect
from .forms import RegisterForm
from account.models import Account
from django.db import IntegrityError
from django.contrib.auth import authenticate , login
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# used for register page
def register(response):
    
    try:
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                userEmail = form.cleaned_data['email']
                print(userEmail)
                if User.objects.filter(email = userEmail).exists(): # if email already exisits in database for users
                    return render(response,"account/registered.html",{"form":form , "emailPresent":True} , )
                    
                else: # if email is unique go here 
                    user = form.save()
        
                    account = Account(
                            email=user.email, user=user, firstName=user.first_name, lastName=user.last_name)
                    account.save()
                    
                    login(response,user)
                    return render(response, 'myapp/landingPage.html')
                # after logging in add redirect page here

    except IntegrityError:
            
            return render(response, 'myapp/landingPage.html')


    form = RegisterForm()
    return render(response, 'account/registered.html', {"form": form})
