"""
GenAI Acknowledgment (Assessment 1 - Assisted Reviewer):
In compliance with Keele University academic integrity policies, I used 
generative AI (Chatgpt) strictly as an assisted code reviewer and debugger. 
I consulted the tool to help diagnose runtime exceptions (such as Tkinter TclError 
and NameError), identify subtle typographical errors that were difficult to spot 
manually, and check function execution flow. I take help to understanding git and how to commit 
push and pull. As well as, i consulted with chatgpt during project architecture work and brainstorming.
All core logic, functional decisions, and final code implementations were independently written, tested, 
and verified by me.

Student Name: Sadia Afroze Zafrin
Student ID: 26032504
"""

#srching using id
def searchItemByID(items,item_ID):
    item_ID = str(item_ID).strip().lower()
    for item in items:
        if str(item.get("item_ID") or "").lower() == item_ID:
            return item
    return None

#srch item by name
def searchItemByName(items,item_name):
    found_items = []
    item_name = str(item_name).strip().lower()

    for item in items:
        name = str(item.get("item_name") or "").lower()
        if item_name and item_name in name:
            found_items.append(item)
    return found_items


# Srch item by category
def searchItemByCategory(items, category):
    found_items = []
    category=str(category).strip().lower()
    for item in items:
        item_category=str(item.get("category") or "").lower()
        if category and category in item_category:
            found_items.append(item)
    return found_items
               

#srch item by color
def searchItemByColor(items, color):
    found_items = []
    color = str(color).strip().lower()
    for item in items:
        item_color = str(item.get("color") or "").lower()
        if color and color in item_color:
            found_items.append(item)
    return found_items
               


#sarch item by brand
def searchItemByBrand(items,brand):
    found_items =[]
    brand = str(brand).strip().lower()
    for item in items:
        item_brand= str(item.get("brand") or "").lower()
        if brand and brand in item_brand:
            found_items.append(item)
    return found_items
               
 
#srch item by location
def searchItemByLocation(items,location):
    found_items=[]
    location=str(location).strip().lower()
    for item in items:
        item_location =str(item.get("location") or"").lower()
        if location and location in item_location:
            found_items.append(item)
    return found_items

#srch item by date
def searchItemByDate(items, date):
    found_items = []
    date = str(date).strip().lower()
    for item in items:
        item_date = str(item.get("date") or "").lower()
        if date and date in item_date:
            found_items.append(item)
    return found_items
               
 

#srch item by combining multiple things
def searchItems(items, category=None, color=None, brand=None,
                location=None, item_ID=None, item_name=None,
                date=None, item_type=None):
    found_items = []
    criteria = {
        "item_ID": item_ID,
        "item_name": item_name,
        "category": category,
        "color": color,
        "brand": brand,
        "location": location,
        "date": date,
        "item_type": item_type
    }

    for item in items:
        matches = True
        for field, keyword in criteria.items():
            if keyword is not None and str(keyword).strip():
                value = str(item.get(field) or "").lower()
                keyword = str(keyword).strip().lower()
                if keyword not in value:
                    matches = False
                    break
        if matches:
            found_items.append(item)
    return found_items