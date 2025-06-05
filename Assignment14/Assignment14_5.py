class BankAccount:
    def __init__(self,acno,name,bal):
        self.account_number = acno
        self.name = name
        self.balance = bal

    def deposit(self,depositAmount):
        self.balance = self.balance + depositAmount

    def withdraw(self,withdrawnAmount):
        if withdrawnAmount > self.balance:
            print("Insufficient Balance")
            return

        self.balance = self.balance - withdrawnAmount

    def displayBalance(self):
        print(f"Your current account balance is {self.balance}")

def main():
    obj = BankAccount(101,"Mahesh",5000)
    obj.displayBalance()    

    obj.deposit(2000)
    obj.displayBalance()    

    obj.withdraw(3000)
    obj.displayBalance()

if __name__ == "__main__":
    main()
