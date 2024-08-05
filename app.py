import pygame 
import broker
import scheduler

pygame.init()

WIDTH  = 1000
HEIGHT = 700
FPS    = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.Clock()

pygame.display.set_caption("E C S C A L I B U R")

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        broker.send(event.type, event)
    keys = pygame.key.get_pressed()
    for binding in broker.keybinds:
        if all(keys[key] for key in binding):
            broker.handle(binding)
    broker.flush()
    return True

def update():
    dt = clock.tick(FPS)
    scheduler.run(scheduler.update, dt)

def render():
    window.fill("black")
    scheduler.run(scheduler.render, window)
    pygame.display.update()

def main():
    scheduler.run(scheduler.launch)
    while events():
        update()
        render()
    scheduler.run(scheduler.finish)
    pygame.quit()

if __name__ == "__main__":
    main()
