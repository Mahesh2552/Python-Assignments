Square = lambda No: No * No

Cube = lambda No: No ** 3

def main():
  Num = int(input("Enter number: "))

  print("Square: ", Square(Num))
  print("Cube: ", Cube(Num))
if __name__ == "__main__":
    main()