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
    loadItems,
    loadReq
)

#import contact rqst functions
from src.core.request_manager import(
    createreq,
    viewReq,
    updateReqStatus,
    replyToReq
)


#create an empty list
items = loadItems()
#load saved contact requests
requests = loadReq()

#fnctn to create a contact rqst
def createContactRequest():
    print("\n--- CREATE CONTACT REQUEST ---")

    #show all available items
    viewAllItems(items)

    #get the item id from the user
    item_id = input("Enter the item ID you are enquiring about: ")

    #get requester details
    requester_name = input("Enter your name: ")
    requester_contact = input("Enter your email or phone: ")
    message = input("Enter your message: ")

    #create the contact request
    new_req = createreq(
        requests,
        items,
        item_id,
        requester_name,
        requester_contact,
        message
    )

    if new_req:
        print("\nContact request created successfully!")
        print("Your request ID is:", new_req["req_id"])
    else:
        print("\nCould not create the request. Please check the item ID and required details.")


#fnctn to view contact rqsts
def viewContactRequests():
    print("\n--- VIEW CONTACT REQUESTS ---")

    #ask which item they want to check
    item_id = input("Enter the item ID: ")

    #get all rqst for that item
    item_requests = viewReq(item_id, requests)

    #check there are any rqst
    if not item_requests:
        print("No contact requests found for this item.")
        return

    #display each request
    for request in item_requests:
        print("\nRequest ID:", request["req_id"])
        print("Requester:", request["requester_name"])
        print("Contact:", request["requester_contact"])
        print("Message:", request["message"])
        print("Status:", request["status"])
        print("Response:", request["response"])


#fnctn to update a contact request
def manageContactRequest():
    print("\n--- MANAGE CONTACT REQUEST ---")

    #show all rqsts
    if not requests:
        print("No contact requests available.")
        return

    for request in requests:
        print("\nRequest ID:", request["req_id"])
        print("Item ID:", request["item_ID"])
        print("Requester:", request["requester_name"])
        print("Status:", request["status"])

    #get the rqst id
    req_id = input("\nEnter the request ID: ")

    #choose a new status
    new_status = input("Enter Accepted or Rejected: ").strip().capitalize()

    #update the rqst status
    updated = updateReqStatus(requests, req_id, new_status)

    if updated:
        print("Contact request status updated successfully!")
    else:
        print("Could not update the request. Check the request ID and status.")


#fnctn to reply to a contact rqst
def replyToContactRequest():
    print("\n--- REPLY TO CONTACT REQUEST ---")

    #check if there are any rqst
    if not requests:
        print("No contact requests available.")
        return

    #show all rqst
    for request in requests:
        print("\nRequest ID:", request["req_id"])
        print("Requester:", request["requester_name"])
        print("Message:", request["message"])
        print("Response:", request["response"])

    #get the rqst id and reply
    req_id = input("\nEnter the request ID: ")
    response = input("Enter your reply: ")

    #save the reply
    replied = replyToReq(requests, req_id, response)

    if replied:
        print("Your reply has been saved successfully!")
    else:
        print("Could not send the reply. Check the request ID and reply.")

#menu for contact rqst
def contactRequestMenu():

    while True:
        print("\n===== CONTACT REQUEST MENU =====")
        print("1. Create a contact request")
        print("2. View contact requests")
        print("3. Accept or reject a request")
        print("4. Reply to a request")
        print("5. Back to main menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            createContactRequest()

        elif choice == "2":
            viewContactRequests()

        elif choice == "3":
            manageContactRequest()

        elif choice == "4":
            replyToContactRequest()

        elif choice == "5":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")

#main menu of ReFind
def mainMenu():

    while True:
        print("\n========== REFIND ==========")
        print("1. View all items")
        print("2. View lost items")
        print("3. View found items")
        print("4. Search for an item")
        print("5. Contact requests")
        print("6. Register a new item")
        print("7. Update an item")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            viewAllItems(items)

        elif choice == "2":
            viewLostItems(items)

        elif choice == "3":
            viewFoundItems(items)

        elif choice == "4":
            searchMenu()

        elif choice == "5":
            contactRequestMenu()

        elif choice == "6":
            registerNewItem()

        elif choice == "7":
            updateItemMenu()

        elif choice == "8":
            print("Thank you for using ReFind!")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")

#fnctn to rgster new item
def registerNewItem():
    print("\n============REGISTER NEW ITEM============")
    print("1. Lost Item")
    print("2. Found Item")

    choice =input("Choose item type: ")

    if choice == "1":
        item_type = "lost"
    elif choice == "2":
        item_type ="found"
    else:
        print("Invalid Choice.")
        return
    #get details from user
    item_name=input("Enter item name: ")
    category=input("Enter category: ")
    color= input("Enter item color: ")
    brand = input("Enter brand: ")
    location =input("Enter location: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    #register items
    new_item =registerItem(items, item_type, item_name, category, color,brand,location,date,description)

    if new_item:
        saveItems(items)
        print("\nItem registered successfully.")
        print("Your item ID is:", new_item["item_ID"])
    else:
        print("\n Could not register the item. please check the details.")



#fnctn to update item details
def updateItemMenu():
    print("\n======= UPDATE ITEM =========")
    #show all items first
    viewAllItems(items)
    if not items:
        return
    item_ID = input("\nEnter the item ID you want to update: ").strip()
    print("\n Which detail do you want to update?")
    print("1. Item name")
    print("2. Category")
    print("3. Color")
    print("4.Brand")
    print("5.Location")
    print("6. Date")
    print("7. Description")
    choice = input("Choose a field: ")
    #match choice with item dictionary key
    fields = {
        "1":"item_name",
        "2":"category",
        "3":"color",
        "4":"brand",
        "5":"location",
        "6":"date",
        "7":"description"
    }
    if choice not in fields:
        print("Invalid choice.")
        return
    new_value = input("Enter the new value: ").strip()
    #update the selected detail
    updated_item = updateItem(items, item_ID, fields[choice], new_value)
    if updated_item:
        saveItems(items)
        print("Changes saved successfully.")


#fnction to srch items
def searchMenu():
    print("\n===== SEARCH ITEMS =====")
    print("Leave a field empty if you don't want to use it.")
    item_ID = input("Enter item ID: ").strip()
    item_name = input("Enter item name: ").strip()
    category= input("Enter category: ").strip()
    color = input("Enter color: ").strip()
    brand = input("Enter brand: ").strip()
    location = input("Enter location: ").strip()
    date =input("Enter date (YYYY-MM-DD): ").strip()
    found_items = searchItems(
        items,
        category=category or None,
        color=color or None,
        brand=brand or None,
        location=location or None,
        item_ID=item_ID or None,
        item_name=item_name or None,
        date=date or None
    )
    if found_items:
        print("\n--- SEARCH RESULTS ---")
        viewAllItems(found_items)
    else:
        print("\nNo matching items found.")

#run ReFind when this file is started
if __name__ == "__main__":
    mainMenu()


