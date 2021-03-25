//pushes all items to page

// window.onload = function() {
//     createStorePage();
//   };

function createStorePage(items, storeID)
{
    splitItems = items.split("|");

    const itemContainer = document.getElementById('itemsContainer');

    for(i = 0; i < splitItems.length - 1; i++)
    {
        itemInfo = splitItems[i].split("{");
        itemName = itemInfo[0];
        itemTraits = itemInfo[1].replace('}', '').split(',');
        itemPrice = itemTraits[0];
        itemQuantity = itemTraits[1];
        itemID = itemTraits[2];

        //make item box
        const itemBox = document.createElement('div');
        itemBox.classList.add('item-display');
        itemContainer.appendChild(itemBox);

        //make img
        const img = document.createElement('img');
        img.src = "https://image.shutterstock.com/image-photo/top-view-three-yellow-bananas-260nw-1875848530.jpg"
        img.classList.add('item-image')
        itemBox.appendChild(img);
        
        //making name box
        const name = document.createElement('p');
        name.classList.add('item-text');
        name.innerText = itemName;
        itemBox.appendChild(name)

        //making price box
        const price = document.createElement('p');
        price.classList.add('item-text');
        price.innerText = "$" + itemPrice + " per";
        itemBox.appendChild(price)

        //making purchasing section
        
    }
}