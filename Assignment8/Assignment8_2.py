''' 
2. Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as “exit from main”.
'''

import threading

def evenFactorSum(num):
    sum = 0
    for i in range(1,num):
        if((num % i == 0 and i % 2 == 0) or (i == 1) ):
            sum = sum + i
    print("Addition of even factors = ", sum)

def oddFactorSum(num):
    sum = 0
    for i in range(1,num):
        if((num % i== 0 and i % 2 == 1) or (i == 1)):
            sum = sum + i
    print("Addition of odd factors = ", sum)

def main():
    no = int(input("Enter a number: "))

    evenfactor = threading.Thread(target=evenFactorSum, args=(no,))
    oddfactor = threading.Thread(target=oddFactorSum, args=(no,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()