def main():
    Age  = int(input("Enter your age: "))
    if Age < 0:
        print("Enter valid age")
        return
    
    if Age < 18:
        print("Not Eligible for vote")
    elif Age >= 18:
        print("Eligible for vote")

if __name__ == "__main__":
    main()