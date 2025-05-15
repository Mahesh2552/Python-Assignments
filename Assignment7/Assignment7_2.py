def DoubleNumber(Number):
    return Number * 2
# DoubleNumber = lamda No : No * 2
def main():
    Size = int(input("Enter number of elements: "))

    Numbers = []
    print("Enter your elements: ")

    for i in range(Size):
        no = int(input())
        Numbers.append(no)
    
    # DoubleList = list(map(DoubleNumber, Numbers))
    DoubleList = list(map(DoubleNumber, Numbers))

    print("Doubled list: ", DoubleList)

if __name__ == "__main__":
    main()