import json


def item_list():
    with open('database\\item.json', 'r') as f:
        itemList = json.load(f)
    return itemList


def item_list_search(_id):
    itemList = item_list()
    return Item(itemList[_id])


def item_list_update(updatedList):
    with open('database\\item.json', 'w') as f:
        f.write(json.dumps(updatedList, indent=4))


class Item:
    def __init__(self, itemDetails: dict):
        self.id = itemDetails["id"]
        self.name = itemDetails["name"]
        self.price = itemDetails["price"]
        self.details = {
            "id": itemDetails["id"],
            "name": itemDetails["name"],
            "price": itemDetails["price"]
        }

    def __repr__(self):
        return f'{self.details}'

    def __getitem__(self, attr):
        return f'{self.details[attr]}'

    def add(self):
        itemList = item_list()
        itemList.update({
            self.id: self.details
        })
        item_list_update(itemList)
