from django.contrib import admin
from .models import *

# Register your models here.
# allows models to be viewed and edited from admin page

admin.site.register(Address)
admin.site.register(Item)
admin.site.register(Nutrition)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(Account)
admin.site.register(Vendor)
