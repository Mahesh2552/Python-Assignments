class Vehicle:
    def __init__(self):
        print("Vehicle")

    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()  
        print("Car is starting...")

def main():
    obj = Car()
    obj.start()


if __name__ == "__main__":
    main()
