from constants import *
from map import *

class MG:    #Class who manage main character movements on the maze

	def __init__(self, map, image):
		self.image = image
		self.map = map
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

	def move_right(self):
		if self.case_x < (COLUMNS - 1):
			if self.map.structure[self.case_x+1][self.case_y] != 'm':
				self.case_x += 1
				self.x = self.case_x * SPRITE_SIZE
				#print(self.x, self.y)
				#print(self.case_x, self.case_y)

	def move_left(self):
		if self.case_x > 0:
			if self.map.structure[self.case_x-1][self.case_y] != 'm':
				self.case_x -= 1
				self.x = self.case_x * SPRITE_SIZE
				#print(self.x, self.y)
				#print(self.case_x, self.case_y)

	def move_up(self):
		if self.case_y > 0:
			if self.map.structure[self.case_x][self.case_y-1] != 'm':
				self.case_y -= 1
				self.y = self.case_y * SPRITE_SIZE
				#print(self.x, self.y)
				#print(self.case_x, self.case_y)

	def move_down(self):
		if self.case_y < (ROWS - 1):
			if self.map.structure[self.case_x][self.case_y+1] != 'm':
				self.case_y += 1
				self.y = self.case_y * SPRITE_SIZE
				#print(self.x, self.y)
				#print(self.case_x, self.case_y)

