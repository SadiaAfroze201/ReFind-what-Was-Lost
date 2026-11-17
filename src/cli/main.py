#import functions of items
from src.core.item_manager import(
    generateItemID,
    createItem,
    registerItem,
    viewAllItems,
    viewFoundItems,
    viewLostItems,
    updateItem,
    updateItemStatus,
    deleteItem
)

#import search functions
from src.core.item_search import(
    searchItemByID,
    searchItemByName,
    searchItemByCategory,
    searchItemByBrand,
    searchItemByColor,
    searchItemByLocation,
    searchItemByDate,
    searchItems

)

#import storage functions
from src.core.storage import(
    saveItems,
    loadItems
)

#create an empty list
items = loadItems()

#testing items
print("\n---ALL ITEMS---")
viewAllItems(items)

#testing searches

#ID
print("\n---SEARCH BY ID")
searchItemByID(items,"L001")

#name
print("\n---SEARCH BY NAME")
searchItemByName(items,"Wallet")

#category
print("\n---SEARCH BY CATEGORY")
searchItemByCategory(items,"Accessories")

#color
print("\n---SEARCH BY COLOR")
searchItemByColor(items,"Brown")

#brand
print("\n---SEARCH BY BRAND")
searchItemByBrand(items,"Gucci")

#location
print("\n---SEARCH BY LOCATION")
searchItemByLocation(items,"Library")

#date
print("\n---SEARCH BY DATE")
searchItemByDate(items,"2026-11-26")

#combined
print("\n---COMBINED SEARCH")
searchItems(items,category="electronics", color= "Black")

#testing json items
print("\n--- SAVE ITEMS----")
saveItems(items)
print("items saved successfully")










