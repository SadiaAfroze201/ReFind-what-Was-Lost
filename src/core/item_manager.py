# GenAI Acknoledgement:
# ChatGPT(OpenAI) is used to support project planning and brainstorming
# and clarify programming concepts
# The application code is writtrn by the student

from datetime import datetime

# generating unique ID
L_count = 0
F_count = 0
def generateItemID(item_type):
    global L_count, F_count
    if item_type == "lost":
        L_count += 1
        return f"L{L_count:03d}"
    elif item_type == "found":
        F_count += 1
        return f"F{F_count:03d}"


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
def createItem(item_type, item_name, category, color, brand, location, date, description, photo=None):
    item_ID = generateItemID(item_type)

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
    item = createItem(item_type, item_name, category, color, brand, location, date, description, photo)
    items.append(item)
    return item

#view registered items
def viewAllItems(items):
    if not items:
        print("There is no registered item")
        return
    print("\n ALL ITEMS")
    for item in items:
        print("\nItem ID:",item["item_ID"])
        print("Name:", item["item_name"])
        print("type:",item["item_type"])
        print("Category:",item["category"])
        print("Color:",item["color"])
        print("Brand:",item["brand"])
        print("Location:",item["location"])
        print("Date:",item["date"])
        print("Description:",item["description"])
        print("Status:",item["status"])


#show lost and found seperately
def viewLostItems(items):
    lost_items=[]
    for item in items:
        if item["item_type"] =="lost":
            lost_items.append(item)
    viewAllItems(lost_items)

def viewFoundItems(items):
    found_items=[]
    for item in items:
        if item["item_type"] =="found":
            found_items.append(item)
    viewAllItems(found_items)

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


