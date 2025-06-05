class Calculator:
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
    
    def add(self):
        return self.no1 + self.no2  

    def subtract(self):
        return self.no1 - self.no2
    
    def multiply(self):
        return self.no1 * self.no2
    
    def divide(self):
        if self.no2 == 0:
            return "Cannot divide by Zero"
        return self.no1 / self.no2
    
def main():
    no1 = float(input("Enter first number: "))
    no2 = float(input("Enter second number: "))
    
    obj = Calculator(no1, no2)
    
    print(f"Addition: {obj.add()}")
    print(f"Subtraction: {obj.subtract()}")
    print(f"Multiplication: {obj.multiply()}")
    print(f"Division: {obj.divide()}")

if __name__ == "__main__":
    main()