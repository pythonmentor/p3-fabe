import pygame
from pygame.locals import *
from map import *

class Game:

    def __init__(self):
        pygame.init()
        map = Map("level.txt")
        map.load_maze()
        map.pos_items()
        map.display()
        

    def run(self):
        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == QUIT:
                    launched = False
                elif event.type == KEYDOWN:
                    if event.type == K_UP:
                        print("haut")
                    elif event.type == K_DOWN:
                        print("bas")
                    elif event.type == K_RIGHT:
                        print("droite")
                    elif event.type == K_LEFT:
                        print("gauche")


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
