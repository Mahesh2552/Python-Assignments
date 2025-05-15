def main():
    Num = int(input("Enter a number: "))
    if Num < 0:
        print("Please enter a positive number.")
        return  
    
    Res = 1

    while(Num > 1):
        Res = Res * Num
        Num -= 1
            
    print("Factorial of ", Num, "is: ", Res)

if __name__ == "__main__":
    main()