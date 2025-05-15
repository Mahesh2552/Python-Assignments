def main():
    Num = int(input("Enter a number: "))
    if Num < 0:
        print("Please enter a positive number.")
        return

    for i in range(1, 11):
        print(Num, "\u00D7",  i, "=", Num * i)

if __name__ == "__main__":
    main()