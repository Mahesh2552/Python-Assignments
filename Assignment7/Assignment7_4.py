from functools import reduce

def Product(No1, No2):
    return No1 * No2
    
# EvenNumber = lambda No : No % 2 == 0

def main():
    Size = int(input("Enter number of elements: "))

    Numbers = []
    print("Enter your elements: ")

    for i in range(Size):
        no = int(input())
        Numbers.append(no)
    
    Result = reduce(Product, Numbers)
    print("Product: ", Result)

if __name__ == "__main__":
    main()