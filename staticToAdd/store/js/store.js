//pushes all items to page
window.onload = function() {
    console.log(7);
  };

function createStorePage(items_display, storeID)
{
    splitItems = items_display.split("|");
    const itemContainer = document.getElementById('itemsContainer');
    for(i = 0; i < splitItems.length - 1; i++)
    {
        itemInfo = splitItems[i].split("{");
        itemName = itemInfo[0];
        itemTraits = itemInfo[1].replace('}', '').split(',');
        itemPrice = itemTraits[0];
        itemQuantity = itemTraits[1];
        itemID = itemTraits[2];
        itemUrl = itemTraits[3]; //change to 3

        //make item box
        const itemBox = document.createElement('div');
        itemBox.classList.add('item-display');
        itemContainer.appendChild(itemBox);

        //make img
        const img = document.createElement('img');
        img.src = itemUrl;
        img.classList.add('item-image');
        itemBox.appendChild(img);
        
        //making name box
        const name = document.createElement('div');
        name.classList.add('item-text');
        name.innerText = itemName.charAt(0).toUpperCase() + itemName.slice(1) + " | " + "$" + itemPrice;
        name.id = itemID;
        itemBox.appendChild(name)

        //making purchasing section
        //quantity circle
        const quantity = document.createElement('div');
        quantity.classList.add("item-quantity");
        quantity.innerText = 0;
        itemBox.appendChild(quantity);

        //plus button
        const plus = document.createElement('button');
        plus.classList.add("fa");
        plus.classList.add("fa-plus");
        plus.classList.add("item-plus");
        itemBox.appendChild(plus);
        plus.onclick = function() 
        {
            onChangeQuantityClick(1, quantity);
        }

        //minus button
        const minus = document.createElement('button');
        minus.classList.add("fa");
        minus.classList.add("fa-minus");
        minus.classList.add("item-minus");
        minus.onclick = function() 
        {
            onChangeQuantityClick(-1, quantity);
        }
        itemBox.appendChild(minus);

        //add to cart button
        const addToCart = document.createElement('button');
        addToCart.classList.add('item-addtocart');
        addToCart.innerText = "Add to cart";
        itemBox.appendChild(addToCart);
        addToCart.onclick = function()
        {
            addItem(quantity, storeID, name);
        }
    }
}

function setSuggestions(items){
    suggestions = [
        "Channel",
        "CodingLab",
        "CodingNepal",
        "YouTube",
        "YouTuber",
        "YouTube Channel",
        "Blogger",
        "Bollywood",
        "Vlogger",
        "Vechiles",
        "Facebook",
        "Freelancer",
        "Facebook Page",
        "Designer",
        "Developer",
        "Web Designer",
        "Web Developer",
        "Login Form in HTML & CSS",
        "How to learn HTML & CSS",
        "How to learn JavaScript",
        "How to became Freelancer",
        "How to became Web Designer",
        "How to start Gaming Channel",
        "How to start YouTube Channel",
        "What does HTML stands for?",
        "What does CSS stands for?",
    ];
    return suggestions;
    
}


function onChangeQuantityClick(change, quantityItem)
{
    var curQuantity = parseInt(quantityItem.innerText);
    var newQuantity = curQuantity + change >= 0 ? curQuantity + change : curQuantity;
    quantityItem.innerText = newQuantity;
}

function addItem(quantityItem, storeID, itemNameBox)
{
    var curQuantity = parseInt(quantityItem.innerText);
    var itemParts = itemNameBox.innerText.split("|");
    var itemName = itemParts[0].trim();
    var itemID = itemNameBox.id;
    addItemToCart(storeID, itemID, curQuantity, itemName);
}