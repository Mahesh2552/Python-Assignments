''' 
1. Write a program which contains one lambda function which accepts one parameter and returns power of two.

Input: 4 Output: 16
Input: 6 Output: 64

'''

Square = lambda No: No * No

def main(): 
   Num = int(input("Enter number: "))

   Ans = Square(Num)
   print("Square of ", Num, " is : ", Ans)


if __name__ == "__main__":
   main()
