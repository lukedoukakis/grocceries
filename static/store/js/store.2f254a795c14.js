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
        itemPrice = itemInfo[1].replace('}', '');

        const itemUI = document.createElement('p');
        itemUI.classList.add('centered-text')
        itemUI.textContent = itemName;

        itemContainer.appendChild(itemUI);
    }
}