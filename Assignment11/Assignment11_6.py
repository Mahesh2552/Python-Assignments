'''
6. Sum of First N Natural Numbers
   Write a recursive function to calculate sum from 1 to n.

   
   sum_n(5) → 15
   
'''
sum = 0
def SumOfNaturalNumbers(n):
   global sum

   if n >= 1:
      sum = sum + n
      n = n - 1
      SumOfNaturalNumbers(n)
   
   return sum

def main():
   Number = int(input("Enter number: "))

   if(Number <= 0):
      print("Invalid Input, Please enter a positive integer.")
      return
   
   Result = SumOfNaturalNumbers(Number)

   print(f"Sum of first {Number} Natural numbers is : {Result}")

if __name__ == "__main__":
   main()