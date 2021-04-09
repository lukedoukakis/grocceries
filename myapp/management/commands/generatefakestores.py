from store.models import Vendor, Item
from mysite.settings import BASE_DIR
import json
from os import path
from django.core.management.base import BaseCommand
from geopy.geocoders import Nominatim
import random
import sys

names = ["Albertdaughters", "TraderBros", "Halffood", "Rastas", "Food4More",
         "Safepassage", "Big Foods", "Targate", "Wallmart", "LoseCo", "WrongAid",
         "FoodCity", "Farmers Market", "Keyless Foods", "Shoppers", "Beach Sand"]

lowLong = -118.22
highLong = -116.51
lowLat = 33.47
highLat = 34.44

categories = ["Groccery Store"]
hours = ["6am - 9pm", "7am - 11pm", "3am - 10pm"]
phoneStarters = ["714", "680", "737"]
descriptions = ["Get grocceries here"]

maxItemsPerStore = 15
items = {
    "bananas" : "https://cdn.pixabay.com/photo/2021/01/06/14/44/banana-5894585_1280.png",
    "Crunch" : "https://static.openfoodfacts.org/images/products/005/844/918/1019/front_en.3.full.jpg",
    "almondMilk" : "https://static.openfoodfacts.org/images/products/086/452/400/0119/front_en.3.full.jpg",
    "organic milk" : "https://live.staticflickr.com/7033/6708778809_625d011112_b.jpg",
    "lettuce" : "https://pixy.org/src/13/134601.jpg",
    "artichoke" : "https://live.staticflickr.com/65535/49977513002_051593601b_b.jpg",
    "ketchup" : "https://pixy.org/src/107/1076174.jpeg",
    "mustard" : "https://live.staticflickr.com/1705/25790565000_5b5ab5e88c.jpg",
    "orange" : "https://p2.piqsels.com/preview/424/486/419/fruits-oranges-thumbnail.jpg",
    "lemon" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXUEqcrQiIOJZUV40NNRr7GSm7J0MJWkWXXA&usqp=CAU",
    "eggs" : "https://live.staticflickr.com/3601/3428862342_639ceedf29_b.jpg",
    "bread" : "https://static.openfoodfacts.org/images/products/007/874/201/2285/front_en.3.full.jpg",
    "tortilla chips" : "https://static.openfoodfacts.org/images/products/008/411/411/2903/front_en.4.full.jpg",
    "parsley" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDCogin6c5JozGlNIt8wxJ85OgBM4x4UNCdNKaqPlSkHykcVLNR8df_iEdVeOVMDW7juU&usqp=CAU",
    "brocooli" : "https://live.staticflickr.com/7150/6828874023_5e90d6d097_b.jpg",
} 

quantityMax = 10
priceMax = 10

def gen_phone():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    return '{}-{}-{}'.format(first, second, last)

#creates fake items for a store
def gen_items(item_count, vendor):
    itemList = []
    for i in range(item_count):
        name, url = random.choice(list(items.items()))
        quantity = random.randint(1,quantityMax)
        price = random.uniform(.99, priceMax)

        newItem = Item(name=name, quantity=quantity, price=price, imgURL=url, vendor=vendor)
        newItem.save()
        itemList.append(newItem)

    return itemList

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('storeCount', type=int, help='Indicates the number of stores to be created')

    def handle(self, *args, **kwargs):
        storeCount = kwargs['storeCount']

        latRange = highLat - lowLat
        longRange = highLong - lowLong

        geolocator = Nominatim(user_agent="Grocceries")
        #generate storeCount amount of stores and then populate db with them
        for i in range(storeCount):
            try:
                name = random.choice(names)

                latitude = lowLat + random.uniform(0, latRange)
                longitude = lowLong + random.uniform(0, longRange)

                location = geolocator.reverse(str(latitude) + ", " + str(longitude))
                tempAdress = location.address.split(", ")
                address = tempAdress[0] + " " + tempAdress[1] + ", " + tempAdress[3] + ", " + tempAdress[4] + " " + tempAdress[5]

                category = random.choice(categories)
                hour = random.choice(hours)
                phone = gen_phone()
                description = random.choice(descriptions)

                newVendor = Vendor(name=name, address=address, latitude=latitude,longitude=longitude,
                                   category=category, hours=hour, phone=phone, description=description)
                newVendor.save()

                #generate items for the list
                storeItems = gen_items(random.randint(1, maxItemsPerStore), newVendor)

                print(name + " generated with " + str(len(storeItems)) + " items")

            except IndexError:
                print("Failed to create 1 store")
                storeCount -= 1

        print("Created " + str(storeCount) + " stores")




        #change the stores.json to relfect newly made stores
        stores = path.join(BASE_DIR, "staticToAdd/map/js", "stores.json")

        masterStoreDict = {}
        masterStoreDict.update({"type": "FeatureCollection"})
        features = []

        # edit data here while still in table form
        for vendor in Vendor.objects.all():
            # get params from postgre table and set them up for json file
            geometry = {
                "type": "Point",
                "coordinates": [float(vendor.longitude), float(vendor.latitude)]
            }
            properties = {
                "category": vendor.category,
                "hours": vendor.hours,
                "description": vendor.description,
                "name": vendor.name,
                "phone": str(vendor.phone),
                "storeid": str(vendor.id)
            }

            # create the individual storeDict for each store entry in database
            storeDict = {}
            storeDict.update({"geometry": geometry})
            storeDict.update({"type": "Feature"})
            storeDict.update({"properties": properties})

            # add store dict to our features
            features.append(storeDict)

        # write features(aka stores) to master list
        masterStoreDict.update({"features": features})

        # write stores to json file
        with open(stores, 'w') as outfile:
            json.dump(masterStoreDict, outfile)

        print("Populated json file")