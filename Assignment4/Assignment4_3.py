'''
3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user.
   Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90.
   Map function will increase each number by 10.
   Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter =[76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000

'''
from functools import reduce

def FilterFunction(No):
   if(No >= 70 and No <= 90):
      return True
   else:
      return False
   
def MapFunction(No):
   return No + 10 

def ReduceFunction(A, B):
   return A * B

def main():
   Size = int(input("Enter number of elements: "))
   if(Size <= 0):
      print("Invalid Input")
      return
   Numbers = []
   print("Enter numbers : ")

   for i in range(Size):
      no = int(input())
      Numbers.append(no)

   print("Input List : ", Numbers)

   FData = list(filter(FilterFunction, Numbers))
   # FData = list(filter(lambda No: (No >= 70 and No <= 90), Numbers))  #Using lambda function
   print("List after filter : ", FData)

   MData = list(map(MapFunction, FData))
   # MData = list(map(lambda No: No + 10, FData))  #Using lambda function
   print("List after map : ", MData)

   RData = reduce(ReduceFunction, MData)
   # RData = reduce(lambda A, B: A * B, MData)  #Using lambda function
   print("Output of reduce : ", RData)


if __name__ == "__main__":
   main()