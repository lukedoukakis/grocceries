from django.db import models

# Create your models here.


# ------------------------------------------------------
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
# ------------------------------------------------------

class AddressTable(models.Model):
    email = models.CharField(max_length=255)        # pk
    address = models.CharField(max_length=255)

    # set id to email
    def __str__(self):
        return self.email


class Item(models.Model):
    itemID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.itemID


class Nutrition(models.Model):
    itemID = models.OneToOneField(Item, on_delete=models.CASCADE)
    calories = models.CharField(max_length=255)
    sodium = models.CharField(max_length=255)
    fat = models.CharField(max_length=255)
    Carbs = models.CharField(max_length=255)
    Protein = models.CharField(max_length=255)

    # set id to id

    def __str__(self):
        return self.itemID


class ShoppingCart(models.Model):
    cartNumber = models.CharField(max_length=255)
    # an item can have many shopping carts and a shopping cart can have many items
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.cartNumber  # set id to cartNumber


class Order(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    driver = models.CharField(max_length=255)


class Account(models.Model):
    password = models.CharField(min_length=8 ,max_length=255, default=False)
    email = models.CharField(max_length=255, default=False)        # pk
    name = models.CharField(max_length=255, default=False)
    phone = models.CharField(max_length=255, default=False)
    primaryAddress = models.CharField(max_length=255, default=False)
    shoppingCart = models.OneToOneField(
        ShoppingCart,
        on_delete=models.CASCADE,
        default=False
    )
    addressTable = models.ManyToManyField(AddressTable, default=False)
    is_driver = models.BooleanField(default=False)
    # one to many//an account can have many orders
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=False)

    # set id to email

    def __str__(self):
        return self.email


class Vendor(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    storeName = models.CharField(max_length=255)
    storeLocation = models.CharField(max_length=255)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
  # set id to id

    def __str__(self):
        return self.id


# represents a table
class Test(models.Model):

    # fields/columns for the table
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    # specifies that the id of an entry will be its number (optional)
    def __str__(self):
        return self.text


# this one takes an entry from another table as a field
class ForeignKeyExample(models.Model):
    name = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
