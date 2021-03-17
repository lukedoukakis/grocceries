# This file will be used by the system to store and draw from data locally.
# For example, when the user logs in, their account data will be stored here so that it can be accessed later whenever we need it.

# Use cases (add whatever necessary):
#   storing account currently logged into, so its data can be accessed and manipulated
#   storing vendor currently being accessed, so that its data can be used for querying maps or item stock
#   storing the current listing of vendors and/or items shown, so the front-end can retrieve and display it

# --------------------------------------------------------------------------------------------------------------------------------------

# Fields in here are static fields, they can be accessed with 'LocalData.fieldname' from wherever (don't need an instantiation).
# We technically don't need this cuz python. But I think it's better to have established fields to read and write to for organization purposes.
class LocalData:

    # intended type: myapp.models.Account
    account = None

    # intended type: myapp.models.Vendor
    vendor = None

    # intended type: myapp.models.ShoppingCart
    shopping_cart = None

    # intended type: List<myapp.models.Vendor>
    listed_vendors = None

    # intended type: List<myapp.models.Items>
    listed_items = None



