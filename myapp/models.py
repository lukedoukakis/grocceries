from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

import uuid

# Create your models here.


# ------------------------------------------------------
# ~~~ FUNCTIONS ~~~

# definition for adding an item
# def add_item(_itemID, _name, _price):
#     item = Item(itemID=_itemID, name=_name, price=_price)
#     item.save()


# ------------------------------------------------------
# ~~~ TABLES ~~~

# NOTES FOR USING THE TABLES IN A PYTHON SCRIPT OR SHELL

# To add via shell:
# from myapp.models import Items
# Item = Items(params)
# Item.save()

# create item and save to the database:
# item = <ModelName>(<parameters>)
# item.save()

# get item from database:
# <ModelName>.objects.get(id=<id of object>)

# get all results in a database (returns QuerySet):
# <ModelName>.objects.all()


class Address(models.Model):
    value = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.value


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="default")
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Nutrition(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    calories = models.CharField(max_length=255)
    sodium = models.CharField(max_length=255)
    fat = models.CharField(max_length=255)
    carbs = models.CharField(max_length=255)
    protein = models.CharField(max_length=255)


class Order(models.Model):
    driver = models.CharField(max_length=255)


class Vendor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255, default="default")
    inventory = models.ManyToManyField(Item)
    address = models.CharField(max_length=255, default="default")
    latitude = models.DecimalField(
        max_digits=30, decimal_places=7, default=0.0)
    longitude = models.DecimalField(
        max_digits=30, decimal_places=7, default=0.0)
    category = models.CharField(max_length=255, default='default')
    hours = models.CharField(max_length=255, default='default')
    phone = PhoneNumberField(null=False, blank=False)
    description = models.TextField(default="default")

# FUNCTIONS

#(item.get_attname('quantity') if item.get_attname('quantity') < 100 else 100)
class CartItem(models.Model):
    vendor = models.OneToOneField(Vendor, null=True,on_delete=models.SET_NULL)
    item = models.OneToOneField(Item, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

class ShoppingCart(models.Model):
    cartItems = models.ManyToManyField(CartItem)
    
def get_vendors(_name, _address, _latitude, _longitude, _category, _phone):

    vendors = Vendor.objects.all()
    if(_name != None):
        vendors = vendors.filter(name=_name)
    if(_address != None):
        vendors = vendors.filter(price=_address)
    if(_latitude != None):
        vendors = vendors.filter(latitudee=_latitude)
    if(_longitude != None):
        vendors = vendors.filter(longitude=_longitude)
    if(_category != None):
        vendors = vendors.filter(category=_category)
    if(_phone != None):
        vendors = vendors.filter(phone=_phone)

    if(vendors.count() < 1):
        throw_error("get_vendors: no vendors found")
    return vendors


# returns QuerySet of items from the given vendor matching the parameters
# if no vendor specified, gets item globally
def get_items(_vendor, _name, _price):

    vendors = Vendor.objects.all()
    if(_name != None):
        vendors = vendors.filter(name=_name)
    if(_address != None):
        vendors = vendors.filter(price=_address)
    if(_latitude != None):
        vendors = vendors.filter(latitudee=_latitude)
    if(_longitude != None):
        vendors = vendors.filter(longitude=_longitude)
    if(_category != None):
        vendors = vendors.filter(category=_category)
    if(_phone != None):
        vendors = vendors.filter(phone=_phone)

    if(vendors.count() < 1):
        throw_error("get_vendors: no vendors found")
    return vendors

    # # returns QuerySet of items from the given vendor matching the parameters
    # # if no vendor specified, gets item globally
def get_items(_vendor, _name, _price):

    if(_vendor == None):
        return get_items_global(_name, _price)

    return _vendor.items.all()

    # return QuerySet of items from the Item table with the given attributes

def get_items_global(_name, _price):

    items = Item.objects.all()
    if(_name != None):
        items = items.filter(name=_name)
    if(_price != None):
        items = items.filter(price=_price)

    if(items.count() < 1):
        throw_error("get_items: no items found")
    return items

def throw_error(msg):
    print(msg)