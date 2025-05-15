'''
3. Write a program which accepts N numbers from user and stores them into a List.
   Return Minimum number from that List.

   Input : Number of elements : 4
   Input Elements : 13  5  45  7
   Output : 5

'''
def Minimum(Nums):
   Min = Nums[0]

   for value in Nums:
      if(value < Min):
         Min = value
   
   return Min 

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

   Res = Minimum(Numbers)

   print("Minimum number is : ",Res)

if __name__ == "__main__":
   main()