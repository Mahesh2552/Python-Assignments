def main():
    No1 = int(input("Enter the first number: "))
    No2 = int(input("Enter the second number: "))

    print("Addition : ", No1 + No2)
    print("Substraction : ", No1 - No2)
    print("Multiplication : ", No1 * No2)
    if No2 == 0:
        print("Division is not possible by 0")
        return
    else:
        print("Division : ", No1 / No2)

if __name__ == "__main__":
    main()