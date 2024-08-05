"""
actor.add[alive]()
actor.add[likes, doggos]()
actor.set[position](10, 13)
actor.set[ate, pizzas](7)
"""
from types import MethodType
from functools import wraps, partial

eindex = dict() # entities mapped to their archetypes and their columns
cindex = dict() # parts mapped to their archetypes and their rows

def new_table(*parts):
    schema = tuple(sorted(parts))
    for index, part in enumerate(schema):
        if part not in cindex: cindex[part] = dict()
        cindex[part][schema] = index
    table = [list() for part in parts]
    return table

def push_actor(ID, *parts):
    for part in parts:
        table[part]
    ...

def decorator(func=None, *, a=10, **params):
    if not func:
        return partial(decorator, **params)
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


from itertools import count

class Actor:
    counter = count()
    dead = list()

    @classmethod
    def spawn(Class):
        if Class.dead:
            actor = Class.dead.pop()
            actor.generation += 1
            return actor
        return Class(next(Class.counter))

    def despawn(self):
        self.dead.append(self)

    def __init__(self, value):
        self.value = value
        self.generation = 0

    __hash__ = lambda self: id(self)


a = Actor.spawn()
print(a.value, a.generation)

b = Actor.spawn()
a.despawn()
c = Actor.spawn()
print(c.value, c.generation)

