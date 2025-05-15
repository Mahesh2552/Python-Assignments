''' 
5. Write a program which accepts one number from user and checks whether number is prime or not.
   Input : 5
   Output : It is Prime Number


'''
def CheckPrime(No):
   i = 2
   is_prime = True  

   while(i <= No/2):
      if(No % i == 0):
         is_prime = False
         break

      i += 1
   
   return is_prime

def main():
   Num = int(input("Enter your number: "))
   if(Num < 0 ):
      print("Please enter a positive number")
      return
   elif (Num == 0):
      print("Please enter number greater than zero")
      return
   elif (Num == 1):
      print("It is neither Prime nor Composite")
      return
   
   Res = CheckPrime(Num)
   if(Res == True):
      print("It is Prime Number")
   else:
      print("It is Not Prime Number")


if __name__ == "__main__":
   main()
