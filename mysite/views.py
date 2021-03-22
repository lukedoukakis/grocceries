from mysite.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as user_logout
from myapp.models import *
import json
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from os import path
from django.db import models

from core import localdata

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
    #load json file here with data
    #why is this staticToAdd here? does not work if its static
    stores = path.join(BASE_DIR, "staticToAdd/map/js", "dynamicStores.json")
    
    masterStoreDict = {}
    masterStoreDict.update({"type": "FeatureCollection"})
    features = []
    
    #edit data here while still in table form
    for vendor in Vendor.objects.all():
        #get params from postgre table and set them up for json file
        geometry = {
            "type" : "Point",
            "coordinates" : [float(vendor.longitude), float(vendor.latitude)]
        }
        properties = {
            "category": vendor.category,
            "hours": vendor.hours ,
            "description": vendor.description ,
            "name": vendor.name ,
            "phone": str(vendor.phone) ,
            "storeid": vendor.storeID
        }

        #create the individual storeDict for each store entry in database
        storeDict = {}
        storeDict.update({"geometry":geometry})
        storeDict.update({"type": "Feature"})
        storeDict.update({"properties":properties})

        #add store dict to our features
        features.append(storeDict)

    #write features(aka stores) to master list
    masterStoreDict.update({"features": features})
    print(masterStoreDict)

    #write stores to json file
    with open(stores, 'w') as outfile:  
        json.dump(masterStoreDict, outfile)

    return render(request, 'map/storelocator.html')

def storePage(request, storeIdentifier):
    print(storeIdentifier)
    return render(request, 'store/storepage.html')


def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
