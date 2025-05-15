def main():
    
    length = int(input("Enter length of rectangle: "))
    if(length <= 0):
        print("Length should be greater than 0")
        return
    
    width = int(input("Enter width of rectangle: "))
    if(width <= 0):
        print("Width should be greater than 0")
        return

    Area = length * width
    Perimeter = 2 * (length + width)

    print("Area : ", Area)
    print("Perimeter : ", Perimeter)

if __name__ == "__main__":
    main()