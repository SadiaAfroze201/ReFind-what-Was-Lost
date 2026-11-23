"""
Generative AI Acknowledgement:
ChatGPT (OpenAI) was used to support the planning and development of this
project through brainstorming, explaining programming concepts, clarifying
technical questions, and providing guidance on Git setup and version control.
All application code was independently written, implemented, and tested by
the student.

Student Name: Sadia Afroze Zafrin
Student ID: 26032504
"""

from src.core.item_manager import viewAllItems
#searching using id
def searchItemByID(items, item_ID):
    for item in items:
        if item["item_ID"].lower()==item_ID.lower():
            print("\n---ITEM FOUND---")
            print("Item ID:",item["item_ID"])
            print("Name:", item["item_name"])
            print("type:",item["item_type"])
            print("Category:",item["category"])
            print("Color:",item["color"])
            print("Brand:",item["brand"])
            print("Location:",item["location"])
            print("Date:",item["date"])
            print("Description:",item["description"])
            print("Status:",item["status"])
            return item
    print("no item found with this id.")
    return None


#search item by name
def searchItemByName(items,item_name):
    found_items =[]
    for item in items:
        if item_name.lower() in item["item_name"].lower():
            found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with that name.")
    return found_items
               
 


#search item by category
def searchItemByCategory(items,category):
    found_items =[]
    for item in items:
        if category.lower() in item["category"].lower():
            found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with that category.")
    return found_items
               

#search item by color
def searchItemByColor(items,color):
    found_items =[]
    for item in items:
        if color.lower() in item["color"].lower():
            found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with that color.")
    return found_items
               


#search item by brand
def searchItemByBrand(items,brand):
    found_items =[]
    for item in items:
        if brand.lower() in item["brand"].lower():
            found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with that brand.")
    return found_items
               
 
#search item by location
def searchItemByLocation(items,location):
    found_items =[]
    for item in items:
        if location.lower() in item["location"].lower():
            found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with that location.")
    return found_items
               


#search item by date
def searchItemByDate(items,date):
    found_items =[]
    for item in items:
        if date.lower() in item["date"].lower():
            found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with that date.")
    return found_items
               
 

#search item by combining multiple descriptions
def searchItems(items,category=None,color=None,brand=None,location=None):
    found_items =[]
    for item in items:
        if category and category.lower() not in item["category"].lower():
            continue

        if color and color.lower() not in item["color"].lower():
                    continue

        if brand and brand.lower() not in item["brand"].lower():
                    continue

        if location and location.lower() not in item["location"].lower():
                    continue
        
        found_items.append(item)
    if found_items:
        print("\n--Search Results----")
        viewAllItems(found_items)
    else:
        print("No item found with found.")
    return found_items
               
