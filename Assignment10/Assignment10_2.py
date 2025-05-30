''' 
2. Lambda with two parameters:
   Write a program which contains one lambda function which accepts two parameters and returns their multiplication.

   
   Input : 4  3   Output : 12  
   Input : 6  3   Output : 18
'''

Multiplication = lambda x, y: x * y

def main():    
    
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
    
   result = Multiplication(num1, num2)
    
   print(f"Multiplication of {num1} and {num2} is: {result}")

if __name__ == "__main__":
   main()