from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as user_logout
from myapp.models import *
from core import localdata
import json

# Create your views here.


def homepage(request):
    return render(request, 'myapp/landingPage.html')

def accountInfoPage(request):
    return render(request, 'profile/accountinfo.html')


def loginRedirect(request):

    # store the logged in account to localdata
    localdata.LocalData.account = request.user.account
    print(localdata.LocalData.account.user.username)

    # redirect to appropriate page
    return render(request, 'myapp/landingPage.html')

def loginPage(request):
    return render(request, 'registration/login.html')

def registerPage(request):
    return render(request, 'account/registered.html')

def logout(request):
    user_logout(request)
    localdata.LocalData.account = None
    return render(request, 'myapp/landingPage.html')

def storeFinderPage(request):
    return render(request, 'map/storelocator.html')

def storePage(request, storeIdentifier):
    print("Store Identifier: " + storeIdentifier)

    store = Vendor.objects.get(storeID = storeIdentifier)
    string = ""

    for Item in store.items.all():
        string += Item.name + "{" + str(Item.price) + "}" + "|"

    context = {
        'items': string
    }

    return render(request, 'store/storepage.html', context)

def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
