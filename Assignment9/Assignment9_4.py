'''
4. Create a Python program that compares execution time of summing numbers from 1 to 10 million using:

    normal function,
    threading, and
    multiprocessing.
'''

import threading
import multiprocessing
import time

def Sum():
    sum = 0

    for i in range(1,1000001):
        sum = sum + i

    print("Sum: ",sum)

def main():
    
    #1. With normal function
    start_time = time.time()
    Sum()
    end_time = time.time()
    print("Execution time with normal function: ",end_time-start_time)

    #2. With threading
    start_time = time.time()
    t = threading.Thread(target=Sum)
    t.start()
    t.join()
    end_time = time.time()
    print("Execution time with thread: ",end_time-start_time)

    # #3. With Multiprocessing
    start_time = time.time()
    p = multiprocessing.Process(target=Sum)
    p.start()
    p.join()
    end_time = time.time()
    print("Execution time with multirocessing: ",end_time-start_time)

if __name__ == "__main__":
    main()