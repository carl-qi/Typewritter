from field import Field, Obj
from word import *
import os
import time

SLEEP_TIME = 0.8

class App:
    def __init__(self):
        pass

    def start_game(self):
        self.field = Field(50, 5)
        words = []
        game_over = False
        
        
        
        
        
        num_loops = 0
        
        while not game_over:
            os.system('clear')
            self.field.show_field()
            print('_' * 120)
            if num_loops % (1.6 // SLEEP_TIME) == 0:
                word = Word(self.field)
                words.append(word)
                        
            for w in words:
                if w.speed >= (num_loops) % 3:
                    if (w.row() + w.speed) > (self.field.row_length - 1):
                        self.end_game()
                        game_over = True
                        break
                    else:
                        w.move(w.row() + 1, w.col())
            
            time.sleep(SLEEP_TIME)
            num_loops += 1
    


    def end_game(self):
        print('YOU LOSER!')

a = App()
a.start_game()

"""
    words[0].remove()
    words.pop(0)
"""
