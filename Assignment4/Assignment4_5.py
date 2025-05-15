''' 
5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user.
   Filter should filter out all prime numbers.
   Map function will multiply each number by 2.
   Reduce will return Maximum number from that list.
   (You can also use normal functions instead of lambda functions.)

Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62

'''

from functools import reduce 

def CheckPrime(No):
   IsPrime = True

   i = 2
   while(i <= No/2):
      if(No % i == 0):
         IsPrime = False
         break
      i += 1
   return IsPrime

def MultiplyByTwo(No):
   return No * 2

def Maximum(A, B):
   if(A > B):
      return A
   else:
      return B

def main():
   Size = int(input("Enter number of elements: "))

   if(Size <= 0):
      print("Invalid Input")
      return
   
   Numbers = []

   print("Enter numbers :")

   for i in range(Size):
      no = int(input())
      Numbers.append(no)
   
   print("Input Numbers : ", Numbers)

   FData = list(filter(CheckPrime, Numbers))
   print("List after filter : ", FData)

   MData = list(map(MultiplyByTwo, FData))
   print("List after map : ", MData)

   RData = reduce(Maximum, MData)
   print("Output of reduce : ", RData)


if __name__ == "__main__":
   main()