from django.shortcuts import render
from myapp.models import CartItem
from store.models import Vendor, Item
from django.contrib.auth.decorators import login_required
from account.models import Account
import uuid

# Create your views here.
def storePage(request, storeIdentifier, searchTerm):
    store = Vendor.objects.get(id=uuid.UUID(storeIdentifier))
    current_user = request.user

    items = Item.objects.filter(vendor=store)
    itemsToDisplay = items if searchTerm == "all" else items.filter(name__icontains=searchTerm)

    print(len(items))
    context = {
        'vendorID': storeIdentifier,
        'vendorName': store.name,
        'vendorAddress': store.address,
        'vendorHours': store.hours,
        'vendorPhone': store.phone,
        'vendorDescription': store.description,
        'itemsToDisplay': itemsToDisplay,
        'numOfItemsDisplay': len(itemsToDisplay),
        'items': items,
        'searchTerm': searchTerm
    }
    return render(request, 'store/storepage.html', context)
    
@login_required
def add_to_cart(request, id, quantity):
    item = get_object_or_404(Item, id=id)
    cart_item = CartItem.object.create(item=item, account=request.user)
    cart_item_qs = CartItem.objects.filter(item=item, account=request.user)
    if cart_item_qs.exists():
        cart_item_qs[0].quantity += quantity
        cart_item_qs.save()
    else:
        cart_item.quantity = quantity
        cart_item.save()
    return redirect("storepage", storeIdentifier=item.vendor.id, searchTerm="all")
    
        
    