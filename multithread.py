import threading, time

key = "lol" #it never changes because getch() in thread1 is useless

def thread1():
    while True:
        key = input() #this simply is almost ignored by interpreter, the only thing it
        #gives is that delays print() unless you press any key
        if key == 'lol':
        	print("this is thread1(), and your input is " + key)
        	
threading.Thread(target = thread1).start()

while True:
    time.sleep(.05)
    print(key)