class Student:
    school_name = "Dada Patil Mahavidyalaya"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def DisplayDetails(self):
        print(f"Neme: {self.name}\nRoll Number: {self.roll_no}\nSchool Name: {Student.school_name}\n")


def main():
    obj = Student("Mahesh",101)
    obj.DisplayDetails()

    Student.school_name = "FC College"
    obj.DisplayDetails()

if __name__ == "__main__":
    main()