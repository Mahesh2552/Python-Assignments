'''
5. Using filter(), map(), and reduce() - max of doubled primes:
   Write a program which contains filter(), map(), and reduce() in it.

    Filter: only prime numbers
    Map: multiply each by 2
    Reduce: return maximum

   
   Input List = [2, 70, 11, 10, 17, 23, 31, 77]  
   After filter = [2, 11, 17, 23, 31]  
   After map    = [4, 22, 34, 46, 62]  
   Output of reduce = 62
   
'''

from functools import reduce

def Prime(num):
   if num < 2:
      return False
   for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
         return False
   return True

def Maximum(x, y):
   if x > y:
      return x
   else:
      return y  
    
def main():
   Size = int(input("Enter number of elements: "))

   Numbers = []
   print("Enter your numbers: ")

   for _ in range(Size):
      no = int(input())
      Numbers.append(no)

   FData = list(filter(Prime, Numbers))
   print("After filter:", FData)

   MData = list(map(lambda x: x * 2, FData))
   print("After map:", MData)

   RData = reduce(Maximum, MData)
   print("Output of reduce:", RData)

if __name__ == "__main__": 
   main()