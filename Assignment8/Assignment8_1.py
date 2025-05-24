'''
1. Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers. 
'''

import threading

def print_even_numbers():
    print("Even Numbers:")
    for i in range(0, 20, 2):
        print(i)


def print_odd_numbers():
    print("Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

def main():

    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads have completed execution.")

if __name__ == "__main__":
    main()
    print("Exit from main.")