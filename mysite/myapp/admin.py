from django.contrib import admin
from .models import Test
from .models import ForeignKeyExample

# Register your models here.
# allows models to be viewed and edited from admin page

admin.site.register(Test)
admin.site.register(ForeignKeyExample)