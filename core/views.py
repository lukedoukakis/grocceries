from django.shortcuts import render
from django.http import HttpResponse

from myapp import models


# get store from coordinates
# get store from name
# get account from email


# retrieve a vendor from the Vendor table
def get_vendor(request):

    # vendor = models.get_vendor(<parameters we have will go here>)

    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")


def get_item_global(request):

    # item = models.get_item(<parameters we have will go here>)

    # example: gets item named "Banana"
    # item = models.get_item_global(_name="Banana", _price=None)
    # print(item.name)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")












