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
