class Employee:
    def __init__(self, name, salary, department):
        self.name = name          # Public 
        self.__salary = salary    # Private 
        self._department = department  # Protected 

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self._department}")

    def get_salary(self):
        return self.__salary

def main():
    emp = Employee("Rahul", 60000, "CS")
    emp.display()
    
    print(f"Employee Name: {emp.name}") #public attribute
    
    print(f"Employee Department: {emp._department}") #protected attribute

    #print(emp.__salary)  #private attribute AttributeError: 'Employee' object has no attribute '__salary'. Did you mean: 'get_salary'?

    print(f"Employee Salary: {emp.get_salary()}")
    
if __name__ == "__main__":
    main()
