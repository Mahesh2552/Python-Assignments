'''
2. Factorial Using Recursion
   Write a recursive function to calculate factorial of a number.

   
   factorial(5) → 120
   
'''

Fact = 1

def Factorial(n):
   global Fact

   if n > 1:
      Fact = Fact * n
      n = n - 1
      Factorial(n)

   return Fact


def main():
   Num = int(input("Enter a number to calculate factorial: "))
   result = Factorial(Num)
   print(Num, "! =", result)   

if __name__ == "__main__":
   main()
