'''
4. Using filter(), map(), and reduce() - sum of squares of even numbers:
   Write a program which contains filter(), map(), and reduce() in it.

    Filter: only even numbers
    Map: square of each
    Reduce: sum

   
   Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]  
   After filter = [2, 4, 4, 2, 8, 10]  
   After map    = [4, 16, 16, 4, 64, 100]  
   Output of reduce = 204
   
'''

from functools import reduce

def main():
   Size = int(input("Enter number of elements: "))

   Numbers = []
   print("Enter your numbers: ")

   for _ in range(Size):
      no = int(input())
      Numbers.append(no)

   FData = list(filter(lambda x: x % 2 == 0, Numbers))
   print("After filter:", FData)

   MData = list(map(lambda x: x ** 2, FData))
   print("After map:", MData)

   RData = reduce(lambda x, y: x + y, MData)
   print("Output of reduce:", RData)

if __name__ == "__main__":
   main()