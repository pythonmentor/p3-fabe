import random
import pygame
from pygame.locals import *
from constants import *
pygame.init()

class Map:

    def __init__(self, filename):
        self.filename = filename
        self.structure = []

    def load_maze(self):
        # loading a maze structure from the txt file
        with open(self.filename, "r") as f:
            for ligne in f:
                line_level = list(ligne)
                line_level = line_level[:-1] # remove last character from line_level list
                self.structure.append(line_level)

    def pos_hero(self):
        # define the initial position of MacGyver
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "d":
                    self.start = (n_ligne, n_col)
                    #print(self.start)"""

    def pos_guardian(self):
        # define the initial position of guardian
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "a":
                    self.finish = (n_ligne, n_col)
                    #print(self.finish)"""

    def pos_items(self):
        # define 3 random positions for items
        self.items_poss = []
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "0":
                    position_items = (n_ligne, n_col)
                    self.items_poss.append(position_items)
        self.pos_items = random.sample(self.items_poss, 3)
        print(self.pos_items)

    def display(self):

        window = pygame.display.set_mode((ROWS*SPRITE_SIZE, COLUMNS*SPRITE_SIZE))
        #window.fill(BACKGROUND_COLOR)

        wall = pygame.image.load('ressource/wall.jpg')
        macgyver = pygame.image.load('ressource/macgyver.png').convert_alpha()
        guardian = pygame.image.load('ressource/Gardien.png').convert_alpha()
        item1 = pygame.image.load('ressource/aiguille.png').convert_alpha()
        item2 = pygame.image.load('ressource/ether.png').convert_alpha()
        item3 = pygame.image.load('ressource/seringue.png').convert_alpha()
        
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                pos_x = n_ligne * SPRITE_SIZE
                pos_y = n_col * SPRITE_SIZE
                if col == "m":
                    window.blit(wall, (pos_x, pos_y))
                elif col == "d":
                    window.blit(macgyver, (self.start))
                elif col == "a":
                    window.blit(guardian, (self.finish))

        object_number = 0
        for x, y in self.pos_items:
            pos_x = x * SPRITE_SIZE
            pos_y = y * SPRITE_SIZE
            if object_number == 0:
                window.blit(item1, (pos_x, pos_y))
                object_number +=1
            elif object_number == 1:
                window.blit(item2, (pos_x, pos_y))               
                object_number +=1
            else:
                window.blit(item3, (pos_x, pos_y))

        pygame.display.flip()

        launched = True
        while launched:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        launched = False

def main():
    map = Map("level.txt")
    map.load_maze()
    print(map.structure)
    map.pos_hero()
    map.pos_guardian()
    map.pos_items()
    map.display()
    

if __name__ == "__main__":
    main()