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

import json
def saveItems(items):
    with open("data/items.json", "w")as file:
        json.dump(items, file, indent=4)


def loadItems():
    try:
        with open("data/items.json", "r") as file:
            items = json.load(file)
            return items
    except FileNotFoundError:
        print("Item file is not found. Starting with an empty list.")
        return[]
    except json.JSONDecodeError:
        print("Items file contains invalid json. starting with an empty list.")
        return[]


#save contact rqsts to the json file
def saveReq(requests):
    with open("data/requests.json", "w") as file:
        json.dump(requests, file, indent=4)


#load contact rqsts from json file
def loadReq():
    try:
        with open("data/requests.json", "r") as file:
            requests = json.load(file)
            return requests

    except FileNotFoundError:
        print("Request file is not found. Starting with an empty list.")
        return []

    except json.JSONDecodeError:
        print("Request file contains invalid json. Starting with an empty list.")
        return []
