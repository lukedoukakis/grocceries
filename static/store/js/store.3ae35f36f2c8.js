//pushes all items to page

// window.onload = function() {
//     createStorePage();
//   };

function createStorePage(items)
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

        const itemUI = document.createElement('p');
        itemUI.classList.add('centered-text')
        itemUI.textContent = "Name: " + itemName + " | Price: " + itemPrice + " | Item Quantity: " + itemQuantity;

        itemContainer.appendChild(itemUI);
    }
}