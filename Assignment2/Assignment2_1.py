''' 1. Create a module named as Arithmetic which contains 4 functions as

    `Add()` for addition,
    `Sub()` for subtraction,
    `Mult()` for multiplication and
    `Div()` for division.
     All functions accept two parameters as number and perform the operation.
     Write one Python program which calls all the functions from Arithmetic module by accepting the parameters from user.
'''

from Arithmetic import Add, Sub, Mult, Div
def main(): 
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Addition = Add(Value1,Value2)
    print("Addition is : ",Addition)

    Substraction = Sub(Value1,Value2)
    print("Substraction is : ",Substraction)

    Multiplication = Mult(Value1,Value2)
    print("Multiplication is : ",Multiplication)

    if(Value2  == 0):
        print("Divisible is not possible by 0")
    else:
        Division = Div(Value1,Value2)
        print("Division is : ",Division)


if __name__ == "__main__":
    main()
