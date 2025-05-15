'''
4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user.
   Filter should filter out all such numbers which are even.
   Map function will calculate its square.
   Reduce will return addition of all that numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
'''

from functools import reduce

def Even(No):
   return (No % 2 == 0)
   
def Square(No):
   return No * No

def Addition(A, B):
   return A + B

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

   FData = list(filter(Even, Numbers))
   # FData = list(filter(lambda No: (No % 2 == 0), Numbers))  #Using lambda function
   print("List after filter : ", FData)

   MData = list(map(Square, FData))
   # MData = list(map(lambda No: No * No, FData))  #Using lambda function
   print("List after map : ", MData)

   RData = reduce(Addition, MData)
   # RData = reduce(lambda A, B: A + B, MData)  #Using lambda function
   print("Output of reduce : ", RData)


if __name__ == "__main__":
   main()