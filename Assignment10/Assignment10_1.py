'''
1. Lambda with one parameter:
   Write a program which contains one lambda function which accepts one parameter and returns power of two.

   
   Input : 4      Output : 16  
   Input : 6      Output : 64
'''

Square = lambda x: x ** 2

def main():
   Number = int(input("Enter a number: "))
   result = Square(Number)
   print(f"Square of {Number} is: {result}")  


if __name__ == "__main__":
   main()