''' 
2. Write a Python program using `multiprocessing.Process` to square a list of numbers using multiple processes.
'''

import multiprocessing

def SquareNumbers(Num):
    result = Num * Num
    print(result, end=' ')

def main():
    Numbers = []

    Size = int(input("Enter number of elements: "))
    print("Enter your numbers: ")

    for _ in range(Size):
        no = int(input())
        Numbers.append(no)

    for num in Numbers:
        p = multiprocessing.Process(target=SquareNumbers, args=(num,))
        p.start()

if __name__ == "__main__":
    main()