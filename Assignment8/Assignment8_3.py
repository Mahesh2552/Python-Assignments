'''
3. Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition.

'''
import threading

def EvenSum(Nums):
    sum = 0

    for num in Nums:
        if num % 2 == 0:
            sum = sum + num
    
    print("EvenSum = ",sum)

def OddSum(Nums):
    sum = 0

    for num in Nums:
        if num % 2 == 1:
            sum = sum + num

    print("OddSum = ",sum)

def main():
    Size = int(input("Enter number of elements: "))

    Numbers = []

    print("Enter Numbers: ")

    for i in range(Size):
        no = int(input())
        Numbers.append(no)

    evenlist = threading.Thread(target = EvenSum, args = (Numbers,))
    oddlist  = threading.Thread(target = OddSum, args = (Numbers,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("End of main")
if __name__ == "__main__":
    main()