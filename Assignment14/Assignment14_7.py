class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()  
        print(f"Subject: {self.subject}\nSalary: {self.salary}")

def main():
    name = input("Enter teacher's name: ")
    age = int(input("Enter age: "))
    subject = input("Enter subject : ")
    salary = float(input("Enter salary: "))

    obj = Teacher(name, age, subject, salary)
    obj.display()

if __name__ == "__main__":
    main()