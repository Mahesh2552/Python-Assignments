class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price
    
def main():
    obj1 = Product("Laptop", 50000)
    obj2 = Product("Smartphone", 50000) 
    obj3 = Product("Tablet", 25000)

    print(f"obj1 == obj2: {obj1 == obj2}")  
    print(f"obj1 == obj3: {obj1 == obj3}")
    print(f"obj2 == obj3: {obj2 == obj3}")

if __name__ == "__main__":
    main()