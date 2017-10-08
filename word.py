from random import randint
from database.database import data
from field import Obj

SPACE = '                        '
#SPACE = '------------------------'
class Word(Obj):
    def __init__(self, field):
        self.speed = randint(1, 3)
        temp = data[randint(0, len(data)-1)]
        self.value = temp + (' ' * (24 - len(temp)))
        super().__init__(field, [0, randint(0, field.col_length)-1])
        self.field.matrix[self.row()][self.col()] = self

    def move(self, row, col):
        if self.field.matrix[row][col] == None:
            self.field.matrix[self.previous_location[0]][self.previous_location[1]] = None
            self.previous_location = [row, col]
            self.location = [row, col]
            spaces = ''
            for _ in range(0, 24 - len(self.value)):
                spaces += '-'
            self.field.matrix[row][col] = self
        elif self.speed > self.field.matrix[row][col].speed:
            self.move(row+1, col)
        else:
            self.field.matrix[row][col].move(row+1, col)

    def remove(self):
        self.field.matrix[self.row()][self.col()] = SPACE

