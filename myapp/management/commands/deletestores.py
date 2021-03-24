from myapp.models import Vendor, Item
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        numberStoresDeleted = 0
        for vendor in Vendor.objects.all():
            vendor.delete()
            numberStoresDeleted += 1

        #if we delete stores, items should no longer exist either
        for item in Item.objects.all():
            item.delete()

        print("Deleted " + str(numberStoresDeleted) + " stores")