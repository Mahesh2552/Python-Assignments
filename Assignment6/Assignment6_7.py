def main(): 
    Numbers = []

    print("Enter 5 numbers: ")

    for i in range(5):
        no = int(input())
        Numbers.append(no)

    Max = Numbers[0]

    for num in Numbers:
        if num > Max:
            Max = num
    
    print("Maximum number is : ", Max)
    
if __name__ == "__main__":
    main()