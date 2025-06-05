'''
3. Sum of Digits
   Write a recursive function to calculate the sum of digits of a number.

   sum_of_digits(1234) → 10
   
'''

sum = 0

def SumOfDigits(num):
   global sum

   if num > 0:
      digit = num % 10
      sum = sum + digit
      num = num // 10
      SumOfDigits(num)
   
   return sum

def main():
   num = int(input("Enter a number : "))
   result = SumOfDigits(num)
   print("Sum of digits of", num, "is:", result)

if __name__ == "__main__":
   main()










