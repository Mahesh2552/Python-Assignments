''' 
2. Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

Input: 4  3 Output: 12
Input: 6  3 Output: 18

'''
Mult = lambda No1,No2: No1 * No2

def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))

    Ans = Mult(Num1, Num2)
    print("Multiplication of ", Num1, " and ", Num2, " is : ", Ans)

if __name__ == "__main__":
    main()