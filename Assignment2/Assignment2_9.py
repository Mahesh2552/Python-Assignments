''' 
9. Write a program which accepts number from user and returns number of digits in that number.
   Input : 5187934
   Output : 7

'''
def NumberOfDigits(No):
   Count = 0

   while(No > 0):
      # print(No)
      Count += 1
      No = int(No / 10)

   return Count

def main():
   Num = int(input("Enter your number : "))

   if(Num < 0 ):
      Num *= -1

   Res = NumberOfDigits(Num)

   print("Your number have ", Res, " digits")
if __name__ == "__main__":
   main()
