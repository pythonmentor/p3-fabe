import pygame
from macgyver import *
from map import *
from pygame.locals import *

class Game:

    def run(self):
        map = Map("level.txt")
        map.load_maze()
        map.pos_items()
        map.pos_guardian()
        map.display(0, 0)
        macg = Macgyver(map)

        continued = True
        while continued:
            for event in pygame.event.get(): #Seeking every events happening while the game is running
                if event.type == pygame.QUIT  or \
                        event.type == KEYDOWN and event.key == K_ESCAPE: # If any of these events is QUIT type
                    continued = False # Loop is stopped and the game windows is closed
                if event.type == pygame.KEYDOWN:
                    # Keyboard touch used to moove MacGyver:
                    if event.key == pygame.K_DOWN: # If ARROW DOWN pressed
                        macg.move_down()
                    if event.key == pygame.K_UP:
                        macg.move_up()
                    if event.key == pygame.K_RIGHT:
                        macg.move_right()
                    if event.key == pygame.K_LEFT:
                        macg.move_left()

                map.display(macg.x, macg.y) # Re-pasting after the events
                macg.check_win() # Check the victory conditions

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
