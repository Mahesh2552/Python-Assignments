'''
1. Create a Python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use `threading.Thread`.
'''

import threading
import time

def PrintNumbers():
    for i in range(1,6):
        print(i)

def main():
    t1 = threading.Thread(target=PrintNumbers)
    t2 = threading.Thread(target=PrintNumbers)
    t3 = threading.Thread(target=PrintNumbers)

    print("Thread 1 execution started: \n")
    t1.start()
    t1.join()
    time.sleep(5)
    print("Thread 1 execution ended: \n")

    print("Thread 2 execution started: \n")
    t2.start()
    t2.join()
    time.sleep(5) 
    print("Thread 2 execution ended: \n")

    print("Thread 3 execution started: \n")
    t3.start()
    t3.join()
    time.sleep(5)
    print("Thread 3 execution ended: \n")

if __name__ == "__main__":
    main()