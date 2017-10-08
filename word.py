from random import randint
from database.database import data
from field import Obj

SPACE = '                        '
class Word(Obj):
    def __init__(self, field, value=None):
        self.speed = randint(1, 2)'
        if value:
            self.value = value
        else:
            self.value = data[randint(0, len(data)-1)]
        super().__init__(self, field, [0, randint(0, field.x_length)-1])
        self.move(self.x_location(), self.y_location())

    def move(self, x, y):
        if field.matrix[x][y] == None:
            self.field.matrix[self.previous_location[0]][self.previous_location[1]] = None
            self.previous_location = [x, y]
            self.location = [x, y]
            spaces = ''
            for _ in range(0, 24 - len(self.value)):
                spaces += ' '
            self.field.matrix[x][y] = Word(self.field, self.value + spaces)
        elif self.speed > self.field.matrix[x][y].speed:
            self.move(x+1, y)
        else:
            self.field.matrix[x][y].move(x+1, y)

    def remove(self):
        self.field.matrix[self.x_location()][self.y_location()] = SPACE

