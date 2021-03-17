from django.shortcuts import render
from django.http import HttpResponse

from myapp import models
from core import localdata


# get store from coordinates
# get store from name
# get account from email


# retrieve vendors from the Vendor table (parameters will be established somewhere)
def get_vendors(request):

    # vendor = models.get_vendor(<parameters we have will go here>)

    # ex: get all vendors with name "Trader Joes"
    vendors = models.get_vendors(_name="Trader Joes", _address=None, _latitude=None, _longitude=None, _category=None, _phone=None)
    print(vendors)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def get_items(request):

    # ex: get all items from vendor "Trader Joes"
    localdata.LocalData.vendor = models.get_vendors(_name="Trader Joes", _address=None, _latitude=None, _longitude=None, _category=None, _phone=None)[0] 
    items = models.get_items(_vendor=localdata.LocalData.vendor, _name=None, _price=None)
    print(localdata.LocalData.vendor.name)
    print(items)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def get_items_global(request):

    # item = models.get_item(<parameters we have will go here>)

    # example: gets items named "Banana"
    items = models.get_items_global(_name="Banana", _price=None)
    print(items)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")












