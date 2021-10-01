import numpy as np
import pygame
class Gobang:
    # Initialize the court
    def __init__(self):
        pygame.init()
        self.court = np.empty((15,15),dtype=object)

    def displayGame(self,resolution):
        window_surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Gobang")
        window_surface.fill((255,255,255))
        pygame.display.update()
        return window_surface