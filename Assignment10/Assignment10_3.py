'''
3. Using filter(), map(), and reduce() - product of selected numbers:
   Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers.

    Filter: numbers ≥ 70 and ≤ 90
    Map: add 10 to each number
    Reduce: return the product of all those numbers

   
   Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]  
   After filter = [76, 89, 86, 90, 70]  
   After map    = [86, 99, 96, 100, 80]  
   Output of reduce = 6538752000
   

'''

from functools import reduce

def main():
   
   Size = int(input("Enter number of elements: "))

   Numbers = []
   print("Enter your numbers: ")

   for _ in range(Size):
      no = int(input())
      Numbers.append(no)

   FData = list(filter(lambda x: x >= 70 and x <= 90, Numbers))
   print("After filter:", FData)

   MData = list(map(lambda x: x + 10,FData))
   print("After map:", MData)

   RData = reduce(lambda x,y: x * y,MData)
   print("Output of reduce:", RData)

if __name__ == "__main__":
   main()