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
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        print("bas")
                    if event.key == K_UP:
                        print("haut")
                    if event.key == K_RIGHT:
                        print("droite")
                    if event.key == K_LEFT:
                        print("gauche")


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
