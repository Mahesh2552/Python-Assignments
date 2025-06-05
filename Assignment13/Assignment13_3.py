class Numbers:
    def __init__(self,val):
        self.Value = val

    def ChkPrime(self):
        if self.Value == 1:
            print("1 is neither prime nor composite")
            return
        for i in range(2,int(self.Value/2) + 1):
            if self.Value % i == 0:
                return False
        
        return True

    def ChkPerfect(self):
        if self.Value ==  self.SumFactors():
            return True
        else:
            return False   
        
    def Factors(self):
        Factors = []
        for i in range(1,self.Value):
            if self.Value % i == 0:
                Factors.append(i)
        
        return Factors
    
    def SumFactors(self):
        factorSum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                factorSum = factorSum + i

        return factorSum

def main():
    number = int(input("Enter your number: "))

    obj1 = Numbers(number)

    isPrime = obj1.ChkPrime()
    if isPrime == True:
        print("Give number is Prime")
    else:
        print("Given number is not Prime")
    
    isPerfect = obj1.ChkPerfect()
    if isPerfect == True:
        print("Give number is Perfect Number")
    else:
        print("Given number is not Perfect Number")

    factors = obj1.Factors()
    print(f"Factors of your number are :{factors} ")

    sumOfFactors = obj1.SumFactors()
    print(f"Sum of factors is :{sumOfFactors} ")


if __name__ == "__main__":
    main()