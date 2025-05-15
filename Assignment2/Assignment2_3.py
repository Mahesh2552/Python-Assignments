'''
3. Write a program which accepts one Number from user and returns its factorial.
   Input : 5
   Output : 120
'''
def Factorial(No):
   Result = 1

   while(No>1):
      Result = Result * No
      No -= 1

   return Result
   

def main():
   Num = int(input("Enter number to find factorial: "))

   if(Num < 0 ):
      print("Please enter number greater than zero")
   else:
      Res = Factorial(Num)

      print("Factorila of ", Num, "is ", Num , "! = ", Res)

if __name__ == "__main__":
   main()