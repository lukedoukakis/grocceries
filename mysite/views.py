from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as user_logout
from store.models import Item
from store.models import Vendor
from myapp.models import CartItem, Address
from account.models import Account
from core import localdata
from .forms import AddressForm
from geopy.geocoders import Nominatim
import uuid
import json

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


def itemPage(request, itemIdentifier):
    if not request.user.is_authenticated:
        return homepage(request)
    item = Item.objects.get(id=uuid.UUID(itemIdentifier))

    context = {
        'itemID': itemIdentifier,
        'itemName': item.name,
    }

    return render(request, 'item/itempage.html', context)


def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def deliveryPage(request,a):
    if not request.user.is_authenticated:
        return homepage(request)
    
    geolocator = Nominatim(user_agent="Grocceries")
    address = a.split(",")
    location = geolocator.geocode(str(address[0]))
    print(location.address)
    location = [location.latitude,location.longitude]
    driverLocation = [33.89066309989026, -117.82630507836775]
    storeLons = []
    storeLats = []
    storeNames = ""

    cartItems = CartItem.objects.filter(account=request.user)
    listOfStoresUsed = []
    for i in cartItems:
        listOfStoresUsed.append(i.item.vendor)
    for store in listOfStoresUsed:
        storeLons.append(float(store.longitude))
        storeLats.append(float(store.latitude))
        storeNames += store.name + ","

    context = {
        'accountLocation': location,
        'driverLocation': driverLocation,
        'storeLons': storeLons,
        'storeLats': storeLats,
    }

    return render(request, 'checkout/delivery.html', context)


def paymentPage(request):

    print("RUNNING PAYMENT PAGE")
    if not request.user.is_authenticated:
        return homepage(request)
    cartItems = CartItem.objects.filter(account=request.user)
    ids = []
    prices = []
    quantity = []
    listOfStoresUsed = []
    names = []
    form = AddressForm()

    if request.method == 'POST':

        form = AddressForm(request.POST)

        if form.is_valid():
            addressValue = form.cleaned_data['value']

            a = Address(account=request.user, value=addressValue)
            a.save()

            return deliveryPage(request, addressValue)
            # after payment page go here

        else:
            form = AddressForm()

    totalPrice = 0
    for i in cartItems:
        listOfStoresUsed.append(i.item.vendor)
        ids.append(str(i.item.id))
        prices.append(float(i.item.price))
        quantity.append(i.quantity)
        names.append(i.item.name)
        totalPrice += i.item.price * i.quantity
    listOfStoresUsed = list(set(listOfStoresUsed))
    itemsOrganizedByStore = [
        [0 for i in range(len(cartItems))] for j in range(len(listOfStoresUsed))]
    for i in range(len(listOfStoresUsed)):
        for j in range(len(cartItems)):
            if cartItems[j].item.vendor.id == listOfStoresUsed[i].id:
                itemsOrganizedByStore[i][j] = cartItems[j]
    for i in range(len(itemsOrganizedByStore)):
        itemsOrganizedByStore[i] = list(set(itemsOrganizedByStore[i]))
        # print(itemsOrganizedByStore)
        # itemsOrganizedByStore[i].pop(0)

    for i in range(len(listOfStoresUsed)):
        listOfStoresUsed[i] = listOfStoresUsed[i].name

    myZip = zip(range(len(listOfStoresUsed)), listOfStoresUsed)
    oZip = zip(range(len(listOfStoresUsed)), listOfStoresUsed)

    json_ids = json.dumps(ids)
    json_prices = json.dumps(prices)
    json_names = json.dumps(names)
    json_quantity = json.dumps(quantity)

    context = {
        'listOfStoresUsed': listOfStoresUsed,
        'cartItems': cartItems,
        'itemsOrganizedByStore': itemsOrganizedByStore,
        'r': myZip,
        'o': oZip,
        'numberOfItems': range(len(cartItems)),
        'ids': json_ids,
        'prices': json_prices,
        'names': json_names,
        'quantities': json_quantity,
        'pricesAndNamesQuantity': zip(prices, names, quantity),
        'quantity': quantity,
        'totalPrice': totalPrice,
        'form': form,
        'testy': "lolol"

    }
    return render(request, 'payment/cardpayment2.html', context)
