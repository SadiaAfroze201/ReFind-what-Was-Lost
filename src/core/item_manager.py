# GenAI Acknoledgement:
# ChatGPT(OpenAI) is used to support project planning and brainstorming
# and clarify programming concepts
# The application code is writtrn by the student

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

def createItem(item_type, item_name, category, color, brand, location, date, description, photo=None):
    #generating item id
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

    item = createItem(item_type, item_name, category, color, brand, location, date, description, photo)

    items.append(item)

    return item
#testing multiple item if they are registering or not

# Create an empty list
items = []

# Register a lost wallet
registerItem(
    items, "lost", "Wallet", "Accessories",
    "Brown", "Gucci", "University Library",
    "2026-11-26", "Brown leather wallet"
)

# Register a found phone
registerItem(
    items, "found", "Phone", "Electronics",
    "Black", "Apple", "University Library",
    "2026-11-26", "Black iPhone"
)

# Display registered items
print("Total items:", len(items))

for item in items:
    print(item["item_ID"])


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

viewAllItems(items)

print("\n==============================")

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

#test
print("\n--- LOST ITEMS---")
viewLostItems(items)
print("\n--- FOUND ITEMS---")
viewFoundItems(items)

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



#test
print("----SEARCH ITEM---")
searchItemByID(items, "L001")
searchItemByID(items, "F001")
searchItemByID(items, "L999")
               
        


