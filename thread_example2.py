import threading
import time

def thread_1():
    while True:
        print("thread 1\n")
        time.sleep(1.0)

t1 = threading.Thread(target = thread_1)
t1.start()

temp = input("user input: ")
