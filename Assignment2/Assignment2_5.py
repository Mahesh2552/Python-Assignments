''' 
5. Write a program which accepts one number from user and checks whether number is prime or not.
   Input : 5
   Output : It is Prime Number


'''
def CheckPrime(No):
   i = 2
   is_prime = True  
   while(i < No/2):
      if(No % i == 0):
         is_prime = False
         break

      i += 1
   
   return is_prime

def main():
   num = int(input("Enter your number: "))

   if(num < 0 ):
      print("Please enter a positive number")

   if(CheckPrime(num)):
      print("Prime number")
   else:
      print("Not Prime number")


if __name__ ==  "__main__":
   main()