from field import Field, Obj
from word import *
import os
import time

SLEEP_TIME = 0.2

class App:
    def __init__(self):
        pass

    def start_game(self):
        self.field = Field(5, 10)
        words = []
        game_over = False
        
        
        
        
        
        num_loops = 0
        
        while not game_over:
            os.system('clear')
            self.field.show_field()
            print('_' * 120)
            if num_loops % (1 // SLEEP_TIME) == 0:
                word = Word(self.field)
                words.append(word)
            num_loops += 1
                        
            for w in words:
                if w.speed == (num_loops * SLEEP_TIME) % 3 + 1:
                    if (w.x_location() + w.speed) > (self.field.x_length - 1):
                        self.end_game()
                        game_over = True
                        break
                    else:
                        w.move(w.x_location() + w.speed, w.y_location())
            
            time.sleep(SLEEP_TIME)
    


    def end_game(self):
        print('YOU LOSER!')

a = App()
a.start_game()

"""
    words[0].remove()
    words.pop(0)
"""
