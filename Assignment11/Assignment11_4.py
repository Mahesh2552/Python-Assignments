'''
4. Power Function Using Recursion
   Write a recursive function to calculate xⁿ.

   
   power(2, 3) → 8
   
'''

ans = 1

def Power(x,n):
    
   global ans

   if n > 0:
      ans = ans * x
      n = n - 1
      Power(x,n)

   return ans

def main():
   Number = int(input("Enter number : "))
   Exponent = int(input("Enter exponent : "))
   Result = Power(Number, Exponent)
   print("Answer: ", Result)
   print(f'power({Number},{Exponent})→ {Result}')
    
if __name__ == "__main__":
   main()