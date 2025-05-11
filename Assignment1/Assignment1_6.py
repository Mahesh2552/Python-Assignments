def CheckNum(num):
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")

if __name__ == "__main__":
    print("Enter a number:")
    no = int(input())

    CheckNum(no)