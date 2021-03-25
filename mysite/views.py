from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as user_logout
from myapp.models import *
from core import localdata
import uuid

# Create your views here.

def homepage(request):
    return render(request, 'myapp/landingPage.html')

def accountInfoPage(request):
    return render(request, 'profile/accountinfo.html')


def loginRedirect(request):
    # store the logged in account to localdata
    localdata.LocalData.account = request.user

    # redirect to appropriate page
    return render(request, 'profile/accountinfo.html')

def loginPage(request):
    return render(request, 'registration/login.html')

def registerPage(request):
    return render(request, 'account/registered.html')

def logout(request):
    user_logout(request)
    localdata.LocalData.account = None
    return render(request, 'myapp/landingPage.html')

def storePage(request, storeIdentifier):
    print("Store Identifier: " + storeIdentifier)

    store = Vendor.objects.get(id = uuid.UUID(storeIdentifier))
    itemNameString = ""
    itemIDString = ""
    for item in store.inventory.all():
        itemNameString += item.name + "{" + str(item.price) + "," + str(item.quantity) + "," + str(item.id) + "," + item.imgURL + "}" + "|"

    context = {
        'vendorID': storeIdentifier,
        'vendorName': store.name,
        'vendorItems': itemNameString,
        'vendorItemIDs': itemIDString,
        'vendorAddress': store.address,
        'vendorCategory': store.category,
        'vendorHours': store.hours,
        'vendorPhone': store.phone,
        'vendorDescription': store.description,
    }

    return render(request, 'store/storepage.html', context)

def itemPage(request, itemIdentifier):

    item = Item.objects.get(id = uuid.UUID(itemIdentifier))

    context = {
        'itemID': itemIdentifier,
        'itemName': item.name,
    }

    return render(request, 'item/itempage.html', context)

def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def paymentPage(request):
    return render(request,"payment/cardPayment.html")


