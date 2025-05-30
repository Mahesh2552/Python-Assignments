'''
3. Create a Python program that uses `multiprocessing.Pool` to compute factorial of numbers in a list.

'''

import multiprocessing

def Factorial(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1

    return res

def main(): 
    Numbers = []
    
    Size = int(input("Enter number of elements: "))
    print("Enter your numbers: ")
    
    for _ in range(Size):
        no = int(input())
        Numbers.append(no)
    
    p = multiprocessing.Pool()
    results = p.map(Factorial, Numbers)
   
    print("Factorials:", results)

if __name__ == "__main__":
    main()