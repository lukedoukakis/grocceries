from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse

import uuid

# Create your models here.
class Vendor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255, default="default")
    address = models.CharField(max_length=255, default="default")
    latitude = models.DecimalField(
        max_digits=30, decimal_places=7, default=0.0)
    longitude = models.DecimalField(
        max_digits=30, decimal_places=7, default=0.0)
    category = models.CharField(max_length=255)
    hours = models.CharField(max_length=255, default='default')
    phone = PhoneNumberField(null=False, blank=False)
    description = models.TextField(default="default")

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, null=True, blank=False)
    name = models.CharField(max_length=255, default="default")
    quantity = models.IntegerField(default=1)
    category = models.CharField(max_length=255, default="Food")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imgURL = models.CharField(max_length=255, default="https://image.shutterstock.com/image-photo/top-view-three-yellow-bananas-260nw-1875848530 .jpg")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("itempage", kwargs={
            'itemIdentifier': self.id
        })
    
    def get_add_to_cart_url(self, quantity):
        return reverse("add-to-cart", kwargs={
            'id': self.id,
            'quantity': 1
        })
