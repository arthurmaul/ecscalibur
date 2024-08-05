import ecscalibur as engine
from ecscalibur import broker, app
import pygame

broker.bind(pygame.K_a)
broker.register(pygame.MOUSEBUTTONDOWN, new=True)

engine.run()
