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


from src.core.storage import saveReq
#function that generate rqst id
def generateReqID(requests):
    #if this is the 1st req give r001
    if not requests:
        return "R001"
    highest_num = 0
    #check ids i have so it doesnt reuse
    for request in requests:
        req_id = request["req_id"]
        num = int(req_id[1:])
        if num > highest_num:
            highest_num = num

    #use next nmbr for the new req id
    nxt_num = highest_num +1
    return f"R{nxt_num:03d}"

#generate function for contact rqst
def createreq(requests, items, item_id, requester_name, requester_contact, message):
    #make sure rqstt is linked to a item that exists
    item_exists = False
    for item in items:
        if item["item_ID"] == item_id:
            item_exists = True
            break
    if not item_exists:
        return None

    #dont create a rqst if required details is missing
    if not requester_name.strip() or not requester_contact.strip() or not message.strip():
        return None

    #give this rqst its own id and save details
    new_req = {
        "req_id": generateReqID(requests),
        "item_ID": item_id,
        "requester_name": requester_name.strip(),
        "requester_contact": requester_contact.strip(),
        "message": message.strip(),
        "status": "Pending",
        "response": ""

    }

    requests.append(new_req)
    #save new rqst so it stays there after closing the app
    saveReq(requests)
    return new_req

#show all contact rqsts for particular item
def viewReq(item_id, requests):
    item_requests =[]

    #find rqsts linked to the selected item
    for request in requests:
        if request["item_ID"] == item_id: item_requests.append(request)
    return item_requests


#update the status of contact rqst
def updateReqStatus(requests,req_id, new_status):
    #only allow accpted or rjcted status
    if new_status not in ["Accepted" , "Rejected"]:
        return False

    #find the rqst that wnt to update
    for request in requests:
        if request["req_id"] == req_id:
            request["status"] = new_status
            #save updated status
            saveReq(requests)
            return True
    #return false if rqst id doesnt exists
    return False

#add rply to contact rqst
def replyToReq(requests, req_id, response):
    #chck that rply is not empty
    if not response.strip():
        return False

    #find the rqst and save rply
    for request in requests:
        if request["req_id"] == req_id:
            request["response"] = response.strip()
            #save the updated reply
            saveReq(requests)
            return True

    #return false if rqst ID doesnt exist
    return False