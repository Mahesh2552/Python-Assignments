def main():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))
    Num3 = int(input("Enter third number: "))

    if (Num1 > Num2):
        if(Num1 > Num3):
            print("Largest number is : ", Num1)
        else:
            print("Largest number is : ", Num3)
    elif (Num2 > Num3):
        if(Num2 > Num1):
            print("Largest number is : ", Num2)
        else:
            print("Largest number is : ", Num3)
            
if __name__ == "__main__":
    main()