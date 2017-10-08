from tkinter import *

def submit_word(*arg):
	"""This function does the 'check' process """

	
	print("First Name: " + e1.get())
	e1.delete(0,END)

master = Tk()
Label(master, text="Enter your Word").grid(row=0)


e1 = Entry(master)
e1.grid(row=0, column=1)
master.bind("<Return>", submit_word)
Button(master, text='Quit', command=master.quit).grid(row=1, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=submit_word).grid(row=1, column=1, sticky=W, pady=4)

mainloop()