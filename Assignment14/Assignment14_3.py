class Book:
    def __init__(self,price):
        self.__price = price

    def setPrice(self,newPrice):
        self.__price = newPrice
    
    def getPrice(self):
        return self.__price
    
def main():
    obj = Book(500)
    print(f"Initial Price: {obj.getPrice()}")

    obj.setPrice(1000)
    print(f"New Price: {obj.getPrice()}")

if __name__ == "__main__":
    main()