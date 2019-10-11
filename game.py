import pygame
from pygame.locals import *
from map import *
from macgyver import *
from constants import *

class Game:

    def run(self):
        map = Map("level.txt")
        map.load_maze()
        map.pos_hero()
        map.pos_items()
        map.pos_guardian()
        map.display(0,0)
        macg = MG(map)
        
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT  or \
                        event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        macg.move_down()
                    if event.key == pygame.K_UP:
                        macg.move_up()
                    if event.key == pygame.K_RIGHT:
                        macg.move_right()
                    if event.key == pygame.K_LEFT:
                        macg.move_left()
                
            map.display(macg.x, macg.y)


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
