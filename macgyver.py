import constants

class MacGyver:    #Class who manage main character movements on the maze
	def __init__(self)
		# define the initial position of MacGyver
		self.position_x = 0
		self.position_y = 0
		self.position_case_x = 0
		self.position_case_y = 0


	def move_right(self, direction):
		if direction == 'right':
			if self.position_x < (constants.COLUMNS - 1):
				self.position_x += 1
				self.position_case_x = (self.position_x * constants.SPRITE_SIZE)

	def move_left(self, direction):
		if direction == 'left':
			if self.position_x > 0 :
				self.position_x -= 1
				self.position_case_x = (self.position_x * constants.SPRITE_SIZE)

	def move_top(self, direction):
		if direction == 'up':
			if self.position_y > 0 :
				self.position_y -= 1
				self.position_case_y = (self.position_y * constants.SPRITE_SIZE)

	def move_bottom(self, direction):
		if direction == 'down':
			if self.position_y < (constants.ROWS - 1):
				self.position_y += 1
				self.position_case_y = (self.position_y * constants.SPRITE_SIZE)