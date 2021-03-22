from myapp.models import Vendor
from mysite.settings import BASE_DIR
import json
from django.conf import settings
from os import path
from django.db import models
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #load json file here with data
        stores = path.join(BASE_DIR, "staticToAdd/map/js", "stores.json")
        
        masterStoreDict = {}
        masterStoreDict.update({"type": "FeatureCollection"})
        features = []
        
        #edit data here while still in table form
        for vendor in Vendor.objects.all():
            #get params from postgre table and set them up for json file
            geometry = {
                "type" : "Point",
                "coordinates" : [float(vendor.longitude), float(vendor.latitude)]
            }
            properties = {
                "category": vendor.category,
                "hours": vendor.hours ,
                "description": vendor.description ,
                "name": vendor.name ,
                "phone": str(vendor.phone) ,
                "storeid": vendor.storeID
            }

            #create the individual storeDict for each store entry in database
            storeDict = {}
            storeDict.update({"geometry":geometry})
            storeDict.update({"type": "Feature"})
            storeDict.update({"properties":properties})

            #add store dict to our features
            features.append(storeDict)

        #write features(aka stores) to master list
        masterStoreDict.update({"features": features})

        #write stores to json file
        with open(stores, 'w') as outfile:  
            json.dump(masterStoreDict, outfile)

        print("Populated json file")