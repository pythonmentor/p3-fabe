class MacGyver:    #Class who manage main character movements on the maze
	def __init__(self, position_x, position_y):
		self.position_x = position_x
		self.position_y = position_y


	def move_right(self, direction):
		if direction == 'right':
			return self.position_x += 1

	def move_left(self, direction):
		if direction == 'left':
			return self.position_x -= 1

	def move_top(self, direction):
		if direction == 'top':
			return self.position_y += 1

	def move_bottom(self, direction):
		if direction == 'bottom':
			return self.position_y -= 1
