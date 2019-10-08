import random
import pygame
from pygame.locals import *
from constants import *

class Map:

    def __init__(self, filename):
        pygame.init()
        self.filename = filename
        self.structure = []
        self.window = pygame.display.set_mode((ROWS*SPRITE_SIZE, COLUMNS*SPRITE_SIZE))

    def load_maze(self):
        # loading a maze structure from the txt file
        with open(self.filename, "r") as f:
            for ligne in f:
                line_level = list(ligne)
                line_level = line_level[:-1] # remove last character from line_level list
                self.structure.append(line_level)

    def pos_hero(self):
        # define position of MacGyver
        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                if case == "d":
                    self.pos_hero = (x, y)

    """def pos_guardian(self):
        # define position of guardian
        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                if case == "a":
                    self.pos_guardian = (x, y)"""

    """def pos_walls(self):
        # define all paths positions
        self.pos_walls = []
        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                if case == "m":
                    walls = (x, y)
                    self.pos_walls.append(walls)"""

    def pos_items(self):
        # define 3 random positions for items
        self.items_poss = []
        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                if case == "0":
                    position_items = (x, y)
                    self.items_poss.append(position_items)
        self.pos_items = random.sample(self.items_poss, 3)

    def display(self, hero_x, hero_y):
        self.window.fill((0,0,0))
        wall = pygame.image.load('ressource/wall.jpg')
        macgyver = pygame.image.load('ressource/MacGyver.png').convert_alpha()
        guardian = pygame.image.load('ressource/Gardien.png').convert_alpha()
        item1 = pygame.image.load('ressource/aiguille.png').convert_alpha()
        item2 = pygame.image.load('ressource/ether.png').convert_alpha()
        item3 = pygame.image.load('ressource/seringue.png').convert_alpha()

        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                pos_x = x * SPRITE_SIZE
                pos_y = y * SPRITE_SIZE
                if case == "m":
                    self.window.blit(wall, (pos_x, pos_y))
                elif case == "d":
                    self.window.blit(macgyver, (hero_x, hero_y))
                elif case == "a":
                    self.window.blit(guardian, (pos_x, pos_y))
        
        object_number = 0
        for (x, y) in self.pos_items:
            pos_x = x * SPRITE_SIZE
            pos_y = y * SPRITE_SIZE
            if object_number == 0:
                self.window.blit(item1, (pos_x, pos_y))               
                object_number +=1
            elif object_number == 1:
                self.window.blit(item2, (pos_x, pos_y))               
                object_number +=1
            elif object_number == 2:
                self.window.blit(item3, (pos_x, pos_y))
        
        pygame.display.flip()