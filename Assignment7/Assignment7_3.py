def EvenNumber(No):
    return (No % 2 == 0)
# EvenNumber = lambda No : No % 2 == 0

def main():
    Size = int(input("Enter number of elements: "))

    Numbers = []
    print("Enter your elements: ")

    for i in range(Size):
        no = int(input())
        Numbers.append(no)
    
    # DoubleList = list(filter(EvenNumber, Numbers))
    DoubleList = list(filter(EvenNumber, Numbers))

    print("Even Numbers: ", DoubleList)

if __name__ == "__main__":
    main()