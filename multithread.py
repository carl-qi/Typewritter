import threading, time

key = "lol" #it never changes because getch() in thread1 is useless

def thread1():
    while True:
        if key == 'lol':
        	print("this is thread1(), and your input is " + key)
        	time.sleep(2)

def z():
	threading.Thread(target = thread1).start()
