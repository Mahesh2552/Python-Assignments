''' 
2. Write a program which accepts N numbers from user and stores them into a List.
   Return Maximum number from that List.

   Input : Number of elements : 7
   Input Elements : 13  5  45  7  4  56  34
   Output : 56

'''

def Maximum(Nums):
   Max = Nums[0]

   for value in Nums:
      if(value > Max):
         Max = value
   
   return Max 

def main():
   Size = int(input("Enter number of elements: "))

   if(Size < 0):
       print("Please enter a valid input")
       return
   
   Numbers = []

   print("Enter numbers : ")
   for i in range(Size):
       no = int(input())
       Numbers.append(no)

   Res = Maximum(Numbers)

   print("Maximum number is : ",Res)

if __name__ == "__main__":
   main()