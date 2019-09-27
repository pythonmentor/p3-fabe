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


    def load_hero(self):
        # define the initial position of MacGyver
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "d":
                    self.start = (n_ligne, n_col)
                    print(self.start)

    def load_guardian(self):
        # define the initial position of guardian
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "a":
                    self.finish = (n_ligne, n_col)
                    print(self.finish)

    def load_items(self):
        # define 3 random positions for items
        self.items_poss = []
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "0":
                    position_items = (n_ligne, n_col)
                    self.items_poss.append(position_items)
        self.items = random.sample(self.items_poss, 3)
        print(self.items)

    """def wall_position(self):
        self.wall_position = []
        for n_ligne, ligne in enumerate(self.structure):
            for n_col, col in enumerate(ligne):
                if col == "m":
                    self.wall_position = (n_ligne, n_col)
                    #print(self.wall_position)"""


    def display(self):

        window = pygame.display.set_mode((ROWS*SPRITE_SIZE, COLUMNS*SPRITE_SIZE))

        wall = pygame.image.load('ressource/wall.jpg')
        macgyver = pygame.image.load('ressource/MacGyver.png').convert_alpha()
        guardian = pygame.image.load('ressource/Gardien.png').convert_alpha()
        item1 = pygame.image.load('ressource/aiguille.png').convert_alpha()
        item2 = pygame.image.load('ressource/ether.png').convert_alpha()
        item3 = pygame.image.load('ressource/seringue.png').convert_alpha()

        n_ligne = 0
        for line in self.structure:
            n_col = 0
            for sprite in line:
                pos_x = n_ligne * SPRITE_SIZE
                pos_y = n_col * SPRITE_SIZE
                if sprite == "m":
                    window.blit(wall, (pos_x, pos_y))
                n_col += 1
            n_ligne +=1
        pygame.display.flip()

        launched = True
        while launched:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        launched = False

                    









def main():
    map = Map("level.txt")
    map.load_maze()
    #print(map.structure)
    #map.load_hero()
    #map.load_guardian()
    #map.load_items()
    map.display()
    

if __name__ == "__main__":
    main()