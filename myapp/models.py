from django.db import models
<<<<<<< Updated upstream
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
=======
from django.contrib.auth.models import User
>>>>>>> Stashed changes
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
    name = models.CharField(
        max_length=255, default="default", primary_key=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


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


<<<<<<< Updated upstream
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have an email")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_superuser(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            first_name=first_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(('password'), max_length=128)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name='date joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    phone = models.CharField(max_length=255,  null=True)
    shoppingCart = models.OneToOneField(
        ShoppingCart, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    is_driver = models.BooleanField(default=False,  null=True)
    # one to many//an account can have many orders
    order = models.ForeignKey(Order, on_delete=models.CASCADE,  null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.username
=======
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True)

    firstName = models.CharField(max_length=255, default='default')
    lastName = models.CharField(max_length=255, default='default')
    phone = models.CharField(max_length=255, default='default')
    shoppingCart = models.OneToOneField(
        ShoppingCart, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    is_driver = models.BooleanField(default=False)
    # one to many//an account can have many orders
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
>>>>>>> Stashed changes

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Vendor(models.Model):
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    name = models.CharField(
        max_length=255, default="default", primary_key=True)
    address = models.CharField(max_length=255, default="default")
    # items = models.ForeignKey(Item, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    latitude = models.DecimalField(
        max_digits=30, decimal_places=7, default=0.0)
    longitude = models.DecimalField(
        max_digits=30, decimal_places=7, default=0.0)
    category = models.CharField(max_length=255, default='default')
    hours = models.CharField(max_length=255, default='default')
    phone = models.CharField(max_length=255, default='default')
    description = models.TextField(default="default")

<<<<<<< Updated upstream
    def __str__(self):
        return self.name


# FUNCTIONS

# def get_vendors(_name, _address, _latitude, _longitude, _category, _phone):
=======

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
>>>>>>> Stashed changes

#     vendors = Vendor.objects.all()
#     if(_name != None):
#         vendors = vendors.filter(name=_name)
#     if(_address != None):
#         vendors = vendors.filter(price=_address)
#     if(_latitude != None):
#         vendors = vendors.filter(latitudee=_latitude)
#     if(_longitude != None):
#         vendors = vendors.filter(longitude=_longitude)
#     if(_category != None):
#         vendors = vendors.filter(category=_category)
#     if(_phone != None):
#         vendors = vendors.filter(phone=_phone)

#     if(vendors.count() < 1):
#         throw_error("get_vendors: no vendors found")
#     return vendors

<<<<<<< Updated upstream
=======
# return QuerySet of items from the Item table with the given attributes


def get_items_global(_name, _price):

    items = Item.objects.all()
    if(_name != None):
        items = items.filter(name=_name)
    if(_price != None):
        items = items.filter(price=_price)
>>>>>>> Stashed changes

# # returns QuerySet of items from the given vendor matching the parameters
# # if no vendor specified, gets item globally
# def get_items(_vendor, _name, _price):

#     if(_vendor == None):
#         return get_items_global(_name, _price)

<<<<<<< Updated upstream
#     # TODO: return vendor's items
#     return _vendor.items.all()

# # return QuerySet of items from the Item table with the given attributes


# def get_items_global(_name, _price):

#     items = Item.objects.all()
#     if(_name != None):
#         items = items.filter(name=_name)
#     if(_price != None):
#         items = items.filter(price=_price)

#     if(items.count() < 1):
#         throw_error("get_items: no items found")
#     return items


=======
>>>>>>> Stashed changes
def throw_error(msg):
    print(msg)
