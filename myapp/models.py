from django.db import models

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
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    calories = models.CharField(max_length=255)
    sodium = models.CharField(max_length=255)
    fat = models.CharField(max_length=255)
    carbs = models.CharField(max_length=255)
    protein = models.CharField(max_length=255)


class ShoppingCart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):
    driver = models.CharField(max_length=255)


class Account(models.Model):
    username = models.CharField(max_length=255, default='default')
    email = models.CharField(max_length=255, default='default')
    firstName = models.CharField(max_length=255, default='default')
    lastName = models.CharField(max_length=255, default='default')
    phone = models.CharField(max_length=255, default='default')
    shoppingCart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    # one to many//an account can have many orders
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name






# FUNCTIONS

def get_vendor(_name, _address):
    
    vendors = Vendor.objects.all()
    if(_name != None):
        vendors = vendors.filter(name=_name)
    if(_address != None):
        vendors = vendors.filter(price=_address)

    if(vendors.count() > 1):
        throw_error("error: more than one result")
    return vendors[0]


# returns item from the given vendor matching the parameters
def get_item(_vendor, _name, _price):

    if(_vendor == None):
        return get_item_global(_name, _price)

    # TODO: return vendor's items

# return item from the Item table with the given attributes
def get_item_global(_name, _price):
    
    items = Item.objects.all()
    if(_name != None):
        items = items.filter(name=_name)
    if(_price != None):
        items = items.filter(price=_price)

    if(items.count() > 1):
        throw_error("error: more than one result")
    return items[0]









def throw_error(msg):
    print(msg)