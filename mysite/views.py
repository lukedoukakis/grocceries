from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as user_logout
from myapp.models import *
from core import localdata
import uuid
from django import template

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

    store = Vendor.objects.get(id=uuid.UUID(storeIdentifier))

    items_all = Item.objects.filter(vendor=store)
    if searchTerm == "all":
        items_display = items_all
    else:
        items_display = items_all.filter(name__icontains=searchTerm)

    itemNameString_all = ""
    itemNameString_display = ""
    for item in items_all:
        itemNameString_all += item.name + "{" + str(item.price) + "," + str(
            item.quantity) + "," + str(item.id) + "," + item.imgURL + "}" + "|"
    for item in items_display:
        itemNameString_display += item.name + "{" + str(item.price) + "," + str(
            item.quantity) + "," + str(item.id) + "," + item.imgURL + "}" + "|"

    context = {
        'vendorID': storeIdentifier,
        'vendorName': store.name,
        'vendorItems_all': itemNameString_all,
        'vendorItems_display': itemNameString_display,
        'vendorAddress': store.address,
        'vendorCategory': store.category,
        'vendorHours': store.hours,
        'vendorPhone': store.phone,
        'vendorDescription': store.description,


        'itemsListed': items_display.count(),
        'searchTerm': searchTerm

    }
    print("items all: " + str(items_all))

    return render(request, 'store/storepage.html', context)


def itemPage(request, itemIdentifier):

    item = Item.objects.get(id=uuid.UUID(itemIdentifier))

    context = {
        'itemID': itemIdentifier,
        'itemName': item.name,
    }

    return render(request, 'item/itempage.html', context)


def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def paymentPage(request):

    cartItems = CartItem.objects.filter(account=request.user)

    prices = []
    quantity = []
    listOfStoresUsed = []
    names = []

    for i in cartItems:
        listOfStoresUsed.append(i.item.vendor.name)
        prices.append(i.item.price)
        quantity.append(i.quantity)
        names.append(i.item.name)

    totalPrice = sum(prices)
    listOfStoresUsed = list(set(listOfStoresUsed))

    itemsOrganizedByStore = [
        [0 for i in range(len(cartItems))] for j in range(len(listOfStoresUsed))]

    for i in range(len(listOfStoresUsed)):
        for j in range(len(cartItems)):
            if cartItems[j].item.vendor.name == listOfStoresUsed[i]:
                itemsOrganizedByStore[i][j] = cartItems[j]

    for i in range(len(itemsOrganizedByStore)):
        itemsOrganizedByStore[i] = list(set(itemsOrganizedByStore[i]))
        itemsOrganizedByStore[i].remove(0)
    myZip = zip(range(len(listOfStoresUsed)), listOfStoresUsed)
    context = {
        'listOfStoresUsed': listOfStoresUsed,
        'cartItems': cartItems,
        'itemsOrganizedByStore': itemsOrganizedByStore,
        'r': myZip,
        'numberOfItems': range(len(cartItems)),
        'pricesAndNamesQuantity': zip(prices, names, quantity),
        'quantity': quantity,
        'totalPrice': totalPrice
    }

    return render(request, 'payment/cardpayment.html', context)
