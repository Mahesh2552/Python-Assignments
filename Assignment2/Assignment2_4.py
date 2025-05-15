'''
4. Write a program which accepts one number from user and returns addition of its factors.
   Input : 12
   Output : 16   (1+2+3+4+6)
'''

def SumOfFactors(Num):
   if(Num < 0):
      Num *= -1

   sum = 0
   i  = 1

   while(i <= Num/2):
      
      if(Num % i == 0):
         sum += i
         
      i += 1

   return sum

def main():
   No = int(input("Enter number:  "))

   sum_of_factors = SumOfFactors(No)

   print("Sum of factors : ", sum_of_factors)
   

if __name__ == "__main__":
   main()