from dataclasses import dataclass as record
from dataclasses import field

new = lambda constructor: field(default_factory=constructor)

@record
class Item:
    name:  str = "unknown"
    value: int = 100
    short: str = "Details are unknown"
    long:  str = "No background provided"

@record
class Bag:
    slots: dict = new(dict)
    def __getitem__(self, item):
        return self.slots[item][-1]
    def __setitem__(self, item, value):
        if item not in self.slots:
            self.slots[item] = list()
        self.slots[item].append(value)
    def __delitem__(self, item):
        self.slots.pop(item)
    def store(self, item):
        self[item.name] = item

@record
class Member:
    bag: Bag = new(Bag)
    gold: int = 1000
    def sell(self, item, buyer):
        transfer(self, buyer, item)
    def buy(self, item, seller):
        transfer(seller, self, item)
    def grab(self, item):
        self.bag.store(item)
    def drop(self, item):
        del self.bag[item.name]

def transfer(seller, buyer, item):
    price = seller.bag[item.name].value
    if not buyer.gold >= price:
        return print(f"You are {price - buyer.gold} short of the needed funds.")
    seller.gold += price
    buyer.gold -= price
    buyer.bag[item.name] = seller.bag[item.name]
    del seller.bag[item.name]


a = Member(Bag())
b = Member(Bag())

sword1 = Item(
    "sword 1",
    1500,
    "simple sword",
    "this sword is quite shoddy, but itll do")
sword2 = Item(
    "sword 2",
    500,
    "simple sword",
    "this sword is quite shoddy, but itll do")
b.grab(sword1)
b.grab(sword2)

b.sell(sword1, a)
b.sell(sword2, a)
print(a)
print(b)

