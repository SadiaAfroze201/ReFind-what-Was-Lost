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
from datetime import datetime

# generating unique ID
# generating unique ID
def generateItemID(item_type, items=None):

    #choose the correct ID letter
    if item_type == "lost":
        prefix = "L"
    elif item_type == "found":
        prefix = "F"
    else:
        return None

    #start checking from zero
    highest_num = 0

    #check existing IDs so they dont get repeated
    if items is None:
        items = []

    for item in items:
        item_id = item["item_ID"]

        if item_id.startswith(prefix):
            num = int(item_id[1:])

            if num > highest_num:
                highest_num = num

    #use the next number for the new ID
    next_num = highest_num + 1

    return f"{prefix}{next_num:03d}"

#validate item type so that only it can register as lost and found
def validateItemType(item_type):
    if item_type not in["lost", "found"]:
        print("Invalid item type. Please choose 'lost' or 'found'.")
        return False
    return True

#validating fields that have to be filled in terms of registering an item
def validateRequiredFields(item_name,category,color,location,description):
    required_fields= [item_name,category,color,location,description]
    for field in required_fields:
        if not field or not field.strip():
            print("Required fields cannot be empty.")
            return False
    return True

#setting date format
def validateDate(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid Date! Please use 'YYYY-MM-DD' format.")
        return False

 #generating item id
def createItem(item_type, item_name, category, color, brand, location, date, description, photo=None, items=None):
    item_ID = generateItemID(item_type, items)

#generating item
    item = {
        "item_ID" : item_ID,
        "item_type" : item_type,
        "item_name" : item_name,
        "category" : category,
        "color" : color,
        "brand" : brand,
        "location" : location,
        "date" : date,
        "description" : description,
        "photo" : photo,
        "status" : item_type.capitalize()
    }
    return item

#registering item
def registerItem(items, item_type, item_name, category, color, brand, location, date, description, photo=None):
    if not validateItemType(item_type):
        return None

    if not validateRequiredFields(item_name,category,color,location,description):
        return None

    if not validateDate(date):
        return None
    item = createItem(item_type, item_name, category, color, brand, location, date, description, photo, items)
    items.append(item)
    return item

#display item details
def displayItems(items):
    for item in items:
        print("\nItem ID:", item["item_ID"])
        print("Name:", item["item_name"])
        print("Type:", item["item_type"])
        print("Category:", item["category"])
        print("Color:", item["color"])
        print("Brand:", item["brand"])
        print("Location:", item["location"])
        print("Date:", item["date"])
        print("Description:", item["description"])
        print("Status:", item["status"])


#view all registered items
def viewAllItems(items):
    if not items:
        print("There are no registered items.")
        return

    print("\n--- ALL ITEMS ---")
    displayItems(items)

#show lost and found seperately
def viewLostItems(items):
    lost_items = []
    for item in items:
        if item["item_type"] == "lost":
            lost_items.append(item)

    print("\n--- LOST ITEMS ---")
    if lost_items:
        displayItems(lost_items)
    else:
        print("No lost items found.")


def viewFoundItems(items):
    found_items = []
    for item in items:
        if item["item_type"] == "found":
            found_items.append(item)

    print("\n--- FOUND ITEMS ---")
    if found_items:
        displayItems(found_items)
    else:
        print("No found items found.")

#updating item info using ID
def updateItem(items, item_ID, field, new_value):
    for item in items:
        if item["item_ID"].lower() == item_ID.lower():
            if field in item and field not in ["item_ID","item_type","status"]:
                item[field] = new_value
                print("Item information updated successfully.")
                return item
            print("Invalid Field. Cannot update this info.")
            return None
    print("No item found with this ID.")
    return None

# updating item status
def updateItemStatus(items, item_ID, new_status):
    valid_status = ["Lost", "Found", "Matched", "Returned"]

    if new_status not in valid_status:
        print("Invalid status.")
        return None

    for item in items:
        if item["item_ID"].lower() == item_ID.lower():
            item["status"] = new_status
            print("Item status updated successfully.")
            return item

    print("No item found with this ID.")
    return None

# Delete an item
def deleteItem(items, item_ID):
    for item in items:
        if item["item_ID"].lower() == item_ID.lower():
            items.remove(item)
            print("Item deleted successfully.")
            return item
    print("No item found with this ID.")
    return None


