import os
import msvcrt

class Field(object):
	def __init__(self, x, y):
		""" decide the x and y coordination."""
		self.x_length = x
		self.y_length = y
		self.matrix = [['-' for _ in range(x)] for _ in range(y)]
	
	def show_field(self):
		for y in range(self.y_length):
			row = ''
			for x in range(self.x_length):
				row += self.matrix[y][x]
			print(row)

class Car(object):
	def __init__(self, name):
		self.name = name
		self.location = [0, 0]
		self.previous_location = [0, 0]

	def x_location(self):
		return self.location[0]

	def y_location(self):
		return self.location[1]

	def move(self, x, y, field):
		field.matrix[self.previous_location[0]][self.previous_location[1]] = '-'
		self.location = [x, y]
		field.matrix[x][y] = '0'
		self.previous_location = [x, y]

class User(object):
	def __init__(self, name, car=None, field=None):
		self.name = name
		self.car = car
		self.field = field
		self.control = False

	def move_car(self, x, y):
		self.car.move(x, y, self.field)

	def control_switch(self):
		self.control = not self.control

def control(field, user, not_control_user):
	while True:
		print(user.name, "is playing")
		field.show_field()
		user_input = ord(msvcrt.getch())
		if user_input == 119:
			user.move_car(user.car.x_location() - 1, user.car.y_location())
		elif user_input == 97:
			user.move_car(user.car.x_location(), user.car.y_location() - 1)
		elif user_input == 115:
			user.move_car(user.car.x_location() + 1, user.car.y_location())
		elif user_input == 100:
			user.move_car(user.car.x_location(), user.car.y_location() + 1)
		elif user_input == 99:
			user, not_control_user = not_control_user, user
		elif user_input == 122:
			break
		else:
			print("wrong input")
			input()
		if user.car.location == not_control_user.car.location:
			print("collided!! You die")
			input()
			break
		os.system('cls')

f = Field(20, 20)
car1 = Car("small car")
car2 = Car("big car")
user1 = User("sangbin", car1, f)
user2 = User("bang", car2, f)

control(f, user1, user2)

