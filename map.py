import random
import pygame
from constants import ROWS, COLUMNS, SPRITE_SIZE


class Map:

    def __init__(self, filename):
        self.filename = filename
        pygame.init()
        self.window = pygame.display.set_mode(
            (ROWS * SPRITE_SIZE, COLUMNS * SPRITE_SIZE)
            )

    def load_maze(self):
        '''loading a maze structure from the txt file'''
        self.structure = []
        with open(self.filename, "r") as f:
            for line in f:
                line_level = list(line)
                line_level = line_level[:-1]
                '''remove last character from line_level list'''
                self.structure.append(line_level)

    def pos_guardian(self):
        '''define position of guardian'''
        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                if case == "a":
                    self.pos_guardian = (x, y)

    def pos_items(self):
        '''define 3 random positions for items'''
        self.items_poss = []
        '''Create an empty list'''
        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                if case == "0":
                    position_items = (x, y)
                    self.items_poss.append(position_items)
                    '''Create a list of possible positions'''
        self.pos_items = random.sample(self.items_poss, 3)
        '''Choose 3 random positions in the list'''

    def display(self, hero_x, hero_y):
        '''Display the maze and its elements'''
        self.window.fill((0, 0, 0))
        wall_img = pygame.image.load('img/wall.jpg')
        backgr_img = pygame.image.load('img/backgr.jpg')
        macgyver_img = pygame.image.load('img/MacGyver.png').convert_alpha()
        guardian_img = pygame.image.load('img/Gardien.png').convert_alpha()
        needle_img = pygame.image.load('img/aiguille.png').convert_alpha()
        ether_img = pygame.image.load('img/ether.png').convert_alpha()
        syringe_img = pygame.image.load('img/seringue.png').convert_alpha()

        self.window.blit(backgr_img, (0, 0))

        for x, col in enumerate(self.structure):
            for y, case in enumerate(col):
                pos_x = x * SPRITE_SIZE
                pos_y = y * SPRITE_SIZE
                if case == "m":
                    self.window.blit(wall_img, (pos_x, pos_y))
                    '''Display a wall image on the maze'''
                elif case == "d":
                    self.window.blit(macgyver_img, (hero_x, hero_y))
                    '''Display Macgyver image on the maze'''
                elif case == "a":
                    self.window.blit(guardian_img, (pos_x, pos_y))
                    '''Display the guardian image on the maze'''

        needle_pos, syringe_pos, ether_pos = self.pos_items
        self.window.blit(needle_img, (needle_pos[0] * SPRITE_SIZE,
                                      needle_pos[1] * SPRITE_SIZE))
        self.window.blit(syringe_img, (syringe_pos[0] * SPRITE_SIZE,
                                       syringe_pos[1] * SPRITE_SIZE))
        self.window.blit(ether_img, (ether_pos[0] * SPRITE_SIZE,
                                     ether_pos[1] * SPRITE_SIZE))

        pygame.display.flip()

    def display_win(self):
        '''Display the victory image'''
        self.window.fill((0, 0, 0))
        win_img = pygame.image.load('img/win.jpg').convert_alpha()
        self.window.blit(win_img, (0, 0))
        pygame.display.flip()

    def display_lose(self):
        '''Display the defeat image'''
        self.window.fill((0, 0, 0))
        lose_img = pygame.image.load('img/game_over.jpg').convert_alpha()
        self.window.blit(lose_img, (0, 0))
        pygame.display.flip()
