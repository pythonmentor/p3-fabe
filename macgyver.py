from constants import *
from map import *

class MG:    #Class who manage main character movements on the maze

	def __init__(self):
		# define the initial position of MacGyver
		self.position_x = 0
		self.position_y = 0

	def move_right(self):
		if self.position_x < (COLUMNS - 1):
			if self.structure[self.position_x + 1][self.position_y] != self.pos_walls:
				self.position_x += 1
				self.position_case_x = (self.position_x * SPRITE_SIZE)

	def move_left(self):
		if self.position_x > 0 :
			if self.structure[self.position_x - 1][self.position_y] != self.pos_walls:
				self.position_x -= 1
				self.position_case_x = (self.position_x * SPRITE_SIZE)

	def move_up(self):
		if self.position_y > 0 :
			if self.structure[self.position_x][self.position_y + 1] != self.pos_walls:
				self.position_y -= 1
				self.position_case_y = (self.position_y * SPRITE_SIZE)

	def move_down(self):
		if self.position_y < (ROWS - 1):
			if self.structure[self.position_x][self.position_y - 1] != self.pos_walls:
				self.position_y += 1
				self.position_case_y = (self.position_y * SPRITE_SIZE)