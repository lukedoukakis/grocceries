from django.contrib import admin
from .models import Test
from .models import ForeignKeyExample
from .models import Address
from .models import Account

# Register your models here.
# allows models to be viewed and edited from admin page

admin.site.register(Test)
admin.site.register(ForeignKeyExample)
admin.site.register(Address)
admin.site.register(Account)