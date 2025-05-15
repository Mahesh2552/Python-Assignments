''' 
10. Write a program which accepts number from user and returns addition of digits in that number.
    Input : 5187934
    Output : 37

'''

def AdditionOfDigits(No):
    Sum = 0

    while(No > 0):
        Digit = int(No % 10)  # 123 % 10 = 3 
        #print(Digit)
        Sum += Digit

        No = No / 10
    
    return Sum

def main():
    Num = int(input("Enter number: "))

    if(Num < 0 ):
        Num *= -1

    Res = AdditionOfDigits(Num)

    print("Addition of digits is : ", Res)

if __name__ == "__main__":
    main()