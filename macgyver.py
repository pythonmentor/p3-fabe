from constants import *

class MG:    #Class who manage main character movements on the maze

	def __init__(self, map):
		self.map = map
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#self.backpack = 0

	def move_right(self):
		if self.case_x < (COLUMNS - 1):
			if self.map.structure[self.case_x+1][self.case_y] != 'm':
				self.case_x += 1
				self.x = self.case_x * SPRITE_SIZE
				self.check_picked()

	def move_left(self):
		if self.case_x > 0:
			if self.map.structure[self.case_x-1][self.case_y] != 'm':
				self.case_x -= 1
				self.x = self.case_x * SPRITE_SIZE
				self.check_picked()

	def move_up(self):
		if self.case_y > 0:
			if self.map.structure[self.case_x][self.case_y-1] != 'm':
				self.case_y -= 1
				self.y = self.case_y * SPRITE_SIZE
				self.check_picked()

	def move_down(self):
		if self.case_y < (ROWS - 1):
			if self.map.structure[self.case_x][self.case_y+1] != 'm':
				self.case_y += 1
				self.y = self.case_y * SPRITE_SIZE
				self.check_picked()

	def check_picked(self):
		for (x, y) in self.map.pos_items:
			if (self.case_x, self.case_y) == self.map.pos_items[0]:
				print("You have a needle")
				self.map.pos_items[0] = (0, 0)
			if (self.case_x, self.case_y) == self.map.pos_items[1]:
				print("You have a syringe")
				self.map.pos_items[1] = (1, 0)
			if (self.case_x, self.case_y) == self.map.pos_items[2]:
				print("You have ether")
				self.map.pos_items[2] = (2, 0)

				#self.backpack.append((self.case_x, self.case_y))



				
		


			