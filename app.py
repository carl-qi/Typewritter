from field import Field, Obj
from word import *
import os
import time

SLEEP_TIME = 0.2

class App:
    def __init__(self):
        self.words = []
        self.stage = 1
        self.score = 0
        self.game_over = False

    def start_game(self):
        self.field = Field(30, 5)
        num_loops = 0
        
        while not self.game_over:
            os.system('clear')
            self.field.show_field()
            print('_' * 120)
            print('Stage {0}'.format(self.stage))
            print('Your score is: {0}'.format(self.score))
            print('Type \'quit\' to QUIT.')

            if num_loops % 2 == 0:
                word = Word(self.field)
                self.words.append(word)
                        
            for w in self.words:
                if w.speed >= (num_loops % 10) * abs(100 - self.stage):
                    if (w.row() + 1) > (self.field.row_length - 1):
                        self.end_game('lose')
                        break
                    else:
                        w.move(w.row() + 1, w.col())
            
            time.sleep(SLEEP_TIME)
            num_loops += 1
    
    def end_game(self, msg):
        if msg == 'quit':
            print('KIND OF LOSER')
        else:
            print('YOU LOSER!')

        print('Final score: {0}'.format(self.score))
        self.game_over = True

    def update_words(self, word):
        for w in self.words:
            if word.lower() == 'quit':
                self.end_game('quit')
                break
            elif word == w.value.strip():
                self.words.remove(w)
                self.field.matrix[w.row()][w.col()] = None
                self.score += 1

                if self.score % 3 == 0:
                    self.stage += 1
                    self.sleep_time -= 0.1