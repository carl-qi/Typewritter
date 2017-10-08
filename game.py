import threading, time
from tkinter import *
from app import *

app = App()

def submit_word(*arg):
	app.update_words(e1.get())
	e1.get()
	e1.delete(0,END)

def btn_quit():
	print('quit')

master = Tk()
Label(master, text="Enter your Word").grid(row=0)


e1 = Entry(master)
e1.grid(row=0, column=1)
master.bind("<Return>", submit_word)
Button(master, text='Quit', command=btn_quit).grid(row=1, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=submit_word).grid(row=1, column=1, sticky=W, pady=4)

def start():
	app.start_game()

threading.Thread(target = start).start()
mainloop()