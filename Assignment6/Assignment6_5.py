def CheckPrime(Num):
    i = 2
    isPrime = True
    while(i <= Num/2):
        if Num % i == 0:
            isPrime = False
            break
        i += 1
    
    return isPrime
    
def main():
    Num = int(input("Enter number: "))

    if(Num < 0):
        print("Please enter a positive number.")
        return

    if CheckPrime(Num):
        print(Num, " is a prime number.")
    else:
        print(Num, " is not a prime number.")

if __name__ == "__main__":
    main()