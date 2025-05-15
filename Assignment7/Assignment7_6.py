def CheckPrime(Num):
    i = 2

    while(i <= Num/2):
        if(Num % i == 0):
            return False
        i += 1

    return True

def main():
    Size = int(input("Enter number of elements: "))

    Numbers = []
    print("Enter your elements: ")

    for i in range(Size):
        no = int(input())
        Numbers.append(no)
    
    PrimeList = list(filter(CheckPrime, Numbers))
    print("Prime Numbers: ", PrimeList)

if __name__ == "__main__":
    main()