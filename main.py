import pygame 
import sys

from pygame import display

from extras import *
from pygame.locals import *

class ventana: 
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((ancho,alto)) 
        pygame.display.set_caption(titulo) 
    
    def rungame(self): 
        while True:
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    sys.exit()
            pygame.display.flip()

if __name__ == "__main__": 
    game = ventana()
    game.rungame()

