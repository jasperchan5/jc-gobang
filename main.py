import pygame,sys
from pygame.locals import QUIT
from gobang import Gobang
# from pygame import *
game = Gobang()
resolution = (800,600)
while True:
    for event in pygame.event.get():
        screen = game.displayGame(resolution)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    