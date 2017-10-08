import threading, time
from app import App
from t_test import gui_game

def thread():
	App().start_game()

threading.Thread(target = thread).start()

gui_game()