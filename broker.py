keybinds = dict()
registry = dict()
enqueued = list()

def bind(function, *keys):
    keybinds[keys] = function

def handle(keys):
    keybinds[keys]()

def register(handler, event):
    if event not in registry:
        registry[event] = list()
    registry[event].append(handler)

def send(event, *args, **kwargs):
    if event not in registry:
        return
    for handler in registry[event]:
        print(f"calling handler: {handler}")
        print(f"given parameters: {args, kwargs}")
        handler(*args, **kwargs)

def defer(event, *args, **kwargs):
    enqueued.append((event, args, kwargs))

def flush():
    for event, args, kwargs in enqueued:
        send(event, *args, **kwargs)
    enqueued.clear()

import pygame
bind(lambda: print("a pressed"), pygame.K_a)
register(lambda *args: ..., pygame.MOUSEBUTTONDOWN)
