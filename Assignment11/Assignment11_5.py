'''

5. Count Zeros in a Number (Recursively)
   Write a recursive function to count how many zeros are in the given number.

   count_zeros(1020300) → 4
   
'''

count = 0

def CountZeros(num):
   global count

   if num > 0:
      digit = num % 10
      if(digit == 0):
         count = count + 1
      num = num // 10
      CountZeros(num)
   
   return count

def main():
   Number = int(input("Enter a number : "))
   result = CountZeros(Number)
   print(f"Number of zeros in {Number} is: {result}")

if __name__ == "__main__":
   main()