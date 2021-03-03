from django.contrib import admin
from .models import *

# Register your models here.
# allows models to be viewed and edited from admin page

admin.site.register(Test)
admin.site.register(ForeignKeyExample)
admin.site.register(AddressTable)
admin.site.register(Account)
admin.site.register(Items)
admin.site.register(Nutrition)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(Vendor)
