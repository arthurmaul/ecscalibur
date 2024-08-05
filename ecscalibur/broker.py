keybinds = dict()
registry = dict()
enqueued = list()

def bind(*keys, action=lambda keys: print(f"keybind {keys} triggered"), override=False):
    if not override and keys in keybinds:
        raise ValueError(f"New keybind for {keys} already exists in the registry. Enable overriding to change binding.")
    keybinds[keys] = action

def handle(keys):
    keybinds[keys](keys)

def register(event, handler=lambda event: print(f"recieved event {event}"), new=False):
    if new and event in registry:
        raise ValueError(f"New event {event} already exists in the registry. Disable event creation to add to existing {event} handler list.")
    if not new and event not in registry:
        raise ValueError(f"New event creation was disabled and {event} was not found in the registry.")
    if new and event not in registry:
        registry[event] = list()
    registry[event].append(handler)

def send(event, *args, **kwargs):
    for handler in registry[event]:
        handler(*args, **kwargs)

def defer(event, *args, **kwargs):
    enqueued.append((event, args, kwargs))

def flush():
    for event, args, kwargs in enqueued:
        send(event, *args, **kwargs)
    enqueued.clear()

