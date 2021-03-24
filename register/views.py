from django.shortcuts import render, redirect
from .forms import AccountCreationForm
from account.models import Account
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate , login
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



# used for register page
def register(request):
    context = {}
    if request.POST:
        form = AccountCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            
            login(request, account)
            return redirect('account')
        else:
            context['registration_form'] = form
            return render(request, 'account/registered.html', context)
            
    elif request.method == "GET":
        form = AccountCreationForm()
        context['registration_form'] = form
    return render(request, 'account/registered.html', context)
