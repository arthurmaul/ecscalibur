"""
markers = dict()
storage = dict()
schemas = dict()
"""
from itertools import count

counter = count()
tableid = count()

registry = dict()

def table(*parts):
    for index, part in enumerate(parts):
        registry[part][parts] = index
    return [list() for part in parts]

def push(destination, actor, *parts):
    for index, part in enumerate(destination):
        part.append(parts[index])

def pull(actor, *parts):
    location, index = registry[actor]

def actor(name=None):
    ID = name or next(counter)
    registry[ID] = dict()
    return ID

def part(name=None):
    return actor(name)

def move(actor):
    ...

def equip(actor, part, target=None, data=None): # target means its a relation, data means its not a tag
    location, index = ..., ...

a = actor()
p1 = part()
p2 = part()
p3 = part()
t = table(p1, p2, p3)
push(t, a, "a", "b", "c")
print(registry)
print(t)
