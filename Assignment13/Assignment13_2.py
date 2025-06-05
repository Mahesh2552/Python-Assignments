class BankAccount:

    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
       print(f"Name : {self.Name}\nAmount: {self.Amount}\n")

    def Deposit(self,depositAmount):
       self.Amount = self.Amount + depositAmount

    def Withdrawn(self,withdrawnAmount):
        if withdrawnAmount > self.Amount:
            print("Insufficient balance!!!")
            return
        self.Amount = self.Amount - withdrawnAmount

    def CalculateInterest(self, time):
        return ((self.Amount * BankAccount.ROI * time)/100)

def main():
    name = input("Enter your name: ")
    amount = float(input("Enter amount: "))

    obj = BankAccount(name,amount)

    choice = 0
   
    print("Enter 1 to Display\nEnter 2 for Deposit\nEnter 3 for Withdrawn\nEnter 4 to calculate interest\nEnter 5 to exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.Display()
    
    elif choice == 2:
        depositAmount = float(input("Enter deposit amount: "))
        obj.Deposit(depositAmount)
        print("Bank detaails after deposit are : ")
        obj.Display()

    elif choice == 3:
        withdrawnAmount = float(input("Enter withdrawn amount: "))
        obj.Withdrawn(withdrawnAmount)
        print("Bank detaails after withdrawn are : ")
        obj.Display()
    
    elif choice == 4:
        time = float(input("Enter time in years: "))
        interest = obj.CalculateInterest(time)
        print("Intereset is : ",interest)
    
    elif choice == 5:
        print("Exiting....")
        return
    
    else:
        print("Enter calid input!!!")

if __name__ == "__main__":
    main()