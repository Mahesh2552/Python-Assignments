'''
4. Write a program which accepts N numbers from user and stores them into a List.
   Accept one another number from user and return frequency of that number from List.

   Input : Number of elements : 11
   Input Elements : 13  5  45  7  4  56  5  34  2  5  65
   Element to search : 5
   Output : 3

'''
def Frequency(Nums, value):
   Count = 0

   for no in Nums:
      if no == value:
         Count += 1

   return Count


def main():
   Numbers = []
   Size = int(input("Enter number of elements: "))

   if(Size <= 0):
      print("Inalid Input")

   else:
      print("Enter numbers : ")
      for i in range(Size):
         no = int(input())
         Numbers.append(no)

      iNo = int(input("Enter number to search: "))
      Res = Frequency(Numbers, iNo)

      print("Frequency of number is : ", Res)


if __name__ == "__main__":
   main()