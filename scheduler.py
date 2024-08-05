launch = list()
update = list()
render = list()
finish = list()

def run(schedule, *args, **kwargs):
    for step in schedule:
        step(*args, **kwargs)

def register(schedule, group):
    schedule.append(group)

def group(*systems):
    def runner(*args, **kwargs):
        for system in systems:
            system(*args, **kwargs)
    runner.systems = systems
    return runner

def compose(*groups):
    return group(*(system
        for each in groups
        for system in each.systems))

