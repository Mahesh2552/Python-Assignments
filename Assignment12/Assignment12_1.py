class Demo:
    Value = 0 #Class variable 

    def __init__(self, num1, num2):
        self.no1 = num1 #Instance variable 
        self.no2 = num2 #Instance variable 
    
    def Fun(self):     #Instance method
        print("Inside Fun")
        print(f"no1 = {self.no1}\nno2 = {self.no2}\n")

    def Gun(self):
        print("Inside Gun")  #Instance method
        print(f"no1 = {self.no1}\nno2 = {self.no2}\n")

def main():
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()