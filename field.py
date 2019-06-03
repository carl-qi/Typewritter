import os

SPACE = '                        '
#SPACE = '------------------------'

class Field(object):
	"""
	Represent field
	
	x: x value of coordination.
	y: y value of coordination.

	the length of each column : 24

	"""
	def __init__(self, row, col):
		""" decide the x and y coordination."""
		self.row_length = row
		self.col_length = col
		self.matrix = [[None for _ in range(col)] for _ in range(row)] 
	
	def show_field(self):
		for r in range(self.row_length):
			line = ''
			for c in range(self.col_length):
				if self.matrix[r][c]:
					line += self.matrix[r][c].value
				else:
					line = line + SPACE
			print(line)

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

	def row(self):
		return self.location[0]

	def col(self):
		return self.location[1]




