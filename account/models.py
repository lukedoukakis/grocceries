from django.db import models
from django.contrib.auth.models import User
from myapp.models import ShoppingCart, Address, Order
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, unique=True)
    email = models.EmailField(null=True, unique=True)
    firstName = models.CharField(max_length=255, default='default')
    lastName = models.CharField(max_length=255, default='default')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    shoppingCart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    is_driver = models.BooleanField(default=False)
    # one to many//an account can have many orders
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.__str__()