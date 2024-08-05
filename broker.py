keybinds = dict()
registry = dict()
enqueued = list()

def bind(*keys, action=lambda: print("key pressed")):
    keybinds[keys] = action

def handle(keys):
    keybinds[keys]()

def register(event, handler, new=True):
    if new and event in registry:
        raise KeyError(f"New event {event} already exists in the registry. Disable event creation to add to existing {event} handler list.")
    if not new and event not in registry:
        raise KeyError(f"New event creation was disabled and {event} was not found in the registry.")
    if new and event not in registry:
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
bind(pygame.K_a)
register(pygame.MOUSEBUTTONDOWN, lambda *args, **kwargs: ...)
register(pygame.MOUSEBUTTONDOWN, lambda *args, **kwargs: ...)
