'''
5. Design python application which contains two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. 
After execution of thread1 gets completed then schedule thread2.

'''

import threading

def PrintNumbersOneToFifty():
    for i in range(1,51):
        print(i)

def PrintNumbersFiftyToOne():
    for i in range(50,0,-1):
        print(i)

def main():
    
    thread1 = threading.Thread(target=PrintNumbersOneToFifty)
    thread2 = threading.Thread(target=PrintNumbersFiftyToOne)

    print("thread1 execution started")
    thread1.start()
    thread1.join()
    print("thread1 execution ends\n")

    print("thread2 execution started")
    thread2.start()
    thread2.join()
    print("thread2 execution ends\n")

    print("End of main")

if __name__ == "__main__":
    main()