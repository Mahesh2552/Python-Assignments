'''
2. Write a program which contains one class named as Circle.
   Circle class contains three instance variables as Radius, Area, Circumference.
   That class contains one class variable as PI which is initialised to 3.14.
   Inside __init__ method initialise all instance variables to 0.0.

There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display().

 Accept() method will accept value of Radius from user.
 CalculateArea() method will calculate area of circle and store it into instance variable Area.
 CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
 Display() method will display value of all the instance variables as Radius, Area, Circumference.

After designing the above class call all instance methods by creating multiple objects.
'''

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius         = 0.0
        self.Area           = 0.0
        self.Circumference  = 0.0
    
    def Accept(self):
        R = int(input("Enter radius od circle: "))
        self.Radius = R

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius *self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius 

    def Display(self):
        print("Radius = ",self.Radius)
        print("Area = ",self.Area)
        print("Circumference = ",self.Circumference)

    
def main():
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()
    