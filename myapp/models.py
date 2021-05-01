from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import Account
from mysite.settings import AUTH_USER_MODEL
from store.models import Vendor, Item

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
# from store.models import Items
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
    account = models.ForeignKey(Account, null=True ,blank=False, on_delete=CASCADE)

    def __str__(self):
        return self.value

class Order(models.Model):
    # Status Choices
    PENDING = 0
    DONE = 1
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done'),
    )

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.SmallIntegerField(default=0, choices=STATUS_CHOICES)
    address = models.CharField(max_length=255,blank=False)
    account = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=False, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    # method overload
    def __str__(self):
        return self.account.username +  "| Order ID: " + str(self.id)

class OrderItem(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, null=True, blank=False, on_delete=CASCADE)
    
    def copy_cart_item(cartitem):
        item = Item.objects.get(id=cartitem.item.id)
        quantity = cartitem.quantity

    def __str__(self):
        return self.item.name + "|" + self.item.vendor.name

class Nutrition(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    calories = models.CharField(max_length=255)
    sodium = models.CharField(max_length=255)
    fat = models.CharField(max_length=255)
    carbs = models.CharField(max_length=255)
    protein = models.CharField(max_length=255)

class CartItem(models.Model):
    item = models.ForeignKey(Item, null=True, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    account = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=False, on_delete=CASCADE)
    
    class Meta:
        unique_together = ('account', 'item')
    
    def __str__(self):
        return self.account.username + "|" + self.item.name + "|" + self.item.vendor.name
    

# FUNCTIONS

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