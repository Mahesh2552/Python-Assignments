def main():
    temp = float(input("Enter temperature in Celsius: "))

    tempF = (temp * 9/5) + 32

    print("Temperature in Fahrenheit: ", tempF, u'\xb0'"F")

if __name__ == "__main__":
    main()