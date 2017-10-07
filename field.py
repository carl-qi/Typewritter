import os
import msvcrt

class Field(object):
	"""
	Represent field
	
	x: x value of coordination.
	y: y value of coordination.

	the length of each column : 24

	"""
	def __init__(self, x, y):
		""" decide the x and y coordination."""
		self.x_length = x
		self.y_length = y
		self.matrix = [['                        ' for _ in range(x)] for _ in range(y)] # longest length
	
	def show_field(self):
		for y in range(self.y_length):
			row = ''
			for x in range(self.x_length):
				row += self.matrix[y][x]
			print(row)

class obj(object):
	""" 
	object in the field.

	attribute:
		word : word object
		field : field the object is belong to
	method:
		move : move
	"""
	def __init__(self, word, field):
		self.word = word # word object
		self.field = field
		self.location = [0, 0]
		self.previous_location = [0, 0]

	def x_location(self):
		return self.location[0]

	def y_location(self):
		return self.location[1]

	def move(self, x, y):
		self.field.matrix[self.previous_location[0]][self.previous_location[1]] = '                        '
		self.location = [x, y]
		self.field.matrix[x][y] = word.value # should change to the string of the word
		self.previous_location = [x, y]



