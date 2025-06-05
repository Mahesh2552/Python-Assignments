class Rectangle:
   
   def __init__(self,l,w):
      self.length = l
      self.width = w

   def Area(self):
      return (self.length * self.width)
   
   def Perimerter(self):
      return (2 * (self.length + self.width))
   
def main():
   obj = Rectangle(10,5)

   A = obj.Area()
   P = obj.Perimerter()

   print(f"Area: {A}, Perimeter: {P}")

if __name__ == "__main__":
   main()