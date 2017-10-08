import os

SPACE = '                        '

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
		self.matrix = [[None for _ in range(x)] for _ in range(y)] 
	
	def show_field(self):
		for y in range(self.y_length):
			row = ''
			for x in range(self.x_length):
				if self.matrix[y][x]:
					row += self.matrix[y][x].value
				else:
					row += SPACE
			print(row)

class Obj(object):
	""" 
	object in the field.

	attribute:
		word : word object
		field : field the object is belong to
	method:
		move : move
	"""
	def __init__(self, field, start_location=[0, 0]):
		self.field = field
		self.location = start_location
		self.previous_location = start_location

	def x_location(self):
		return self.location[0]

	def y_location(self):
		return self.location[1]




