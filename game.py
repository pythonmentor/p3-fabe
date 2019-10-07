import pygame
from pygame.locals import *
from map import *
from macgyver import *
from constants import *

class Game:

    def __init__(self):
       
        pygame.init()

    def run(self):
        map = Map("level.txt")
        map.load_maze()
        map.pos_items()
        window = pygame.display.set_mode((ROWS*SPRITE_SIZE, COLUMNS*SPRITE_SIZE))
        pygame.display.set_caption("Save MacGyver")
        map.display(window)
        macg = MG(map)
        
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

            window.fill((0, 0, 0))
            map.display(window)            
            window.blit(pygame.image.load('ressource/Macgyver.png').convert_alpha(), (macg.x, macg.y))
            pygame.display.update()

            item1_picked = False
            if (macg.x, macg.y) == map.pos_items[0]:
                item1_picked = True
                window.blit(map.display.item1, (90, 0))

            item2_picked = False
            if (macg.x, macg.y) == map.pos_items[1]:
                item1_picked = True
                window.blit(map.display.item2, (120, 0))

            item3_picked = False
            if (macg.x, macg.y) == map.pos_items[2]:
                item1_picked = True
                window.blit(map.display.item3, (150, 0))
            
            pygame.display.flip()




def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
