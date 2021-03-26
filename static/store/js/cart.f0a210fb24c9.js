//on load
$(function() {
    //clearCart();
    populateCartFromCookie();
    readCookie();
    });

//on unload
window.onbeforeunload = function(){
    //setCartCookie(30);
};

shoppingCart = {};
shoppingCartName = " shoppingCart";

//call this to set cart with dict
function setCartCookie(days)
{
    var date, expires;
    if (days) {
        date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires="+date.toUTCString();
    } else {
        expires = "";
    }

    stringCart = JSON.stringify(shoppingCart);
    document.cookie = "shoppingCart=" + stringCart + "; path=/" + expires;
}

function readCookie()
{
    const cookies = document.cookie;
}

//resets cart to nothing
function clearCart()
{
    document.cookie = "shoppingCart={}" + ";expires=Thu, 01 Jan 1970 00:00:00 UTC" + "; path=/";
}

//populates the shopping cart via the cookie
function populateCartFromCookie()
{
    var cookieData = document.cookie;
    splitCookies = cookieData.split(';')

    for( i = 0; i < splitCookies.length; i++)
    {
        curCookie = splitCookies[i];
        cookieParts = curCookie.split('=');
        if(cookieParts[0] == shoppingCartName)
        {
            //if cart is empty we need to not parse it
            try
            {
                shoppingCart = JSON.parse(cookieParts[1]);
                break;
            }
            catch
            {
                shoppingCart = {};
            }
        }
    }
    console.log(shoppingCart);
}

//removes an item from the cart
//TODO untested code here
function removeItemFromCart(storeID, itemID)
{
    //checks if the store exists
    if(!(storeID in shoppingCart))
    {
        return("Store does not exist in shopping cart");
    }

    var items = shoppingCart[storeID];
    var indexOfItem = -1;
    for(i = 0; i < items.length; i++)
    {
        itemParts = items[i].split(',');
        //if the item exists
        if(itemParts[2] == itemID)
        {
            indexOfItem = i;
        }
    }

    //item exists and needs to be removed
    if(indexOfItem != -1)
    {
        items.splice(indexOfItem, 1);
        shoppingCart[storeID] = items;
        setCartCookie(30);
    }
    else
    {
        return("Item does not exist for the given store");
    }
}

//adds an item to the cart and saves the cookie
function addItemToCart(storeID, itemID, quantity, itemName)
{

    if(quantity <= 0)
    {
        console.log("Item quantity cannot be 0");
        return;
    }

    console.log("Added " + quantity + " " + itemName + " to cart");

    //check if key exists
    if(!(storeID in shoppingCart))
    {
        shoppingCart[storeID] = [];
    }

    //need to check if item already exists in cart otherwise add
    var items = shoppingCart[storeID];
    var itemExists = false;
    for(i = 0; i < items.length; i++)
    {
        itemParts = items[i].split(',');
        //if the item exists
        if(itemParts[0] == itemName)
        {
            itemExists = true;
            var newItemCount = quantity + parseInt(itemParts[1]);
            var newItemInfo = itemName + "," + newItemCount + "," + itemID;
            items[i] = newItemInfo; 
        }
    }
    
    //if the item doesnt exist
    if(!itemExists)
    {
        var itemInfo = itemName + "," + quantity + "," + itemID;
        items.push(itemInfo);
    }
    
    shoppingCart[storeID] = items;
    setCartCookie(30);
}