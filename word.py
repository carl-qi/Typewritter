from random import randint
from database.database import data

class Word:
    def __init__(self):
        self.speed = randint(1, 3)
        self.value = data(randint(0, len(data-1)))
