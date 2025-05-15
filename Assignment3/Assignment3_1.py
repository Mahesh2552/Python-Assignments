''' 
1. Write a program which accepts N numbers from user and stores them into a List.
   Return addition of all elements from that List.

   Input : Number of elements : 6
   Input Elements : 13  5  45  7  4  56
   Output : 130

'''
def Addition(Nums):
    Sum = 0
    
    for item in Nums:
        Sum += item

    # for i in range(len(Nums)):
    #     Sum += Nums[i]

    return Sum

def main():
    Size = int(input("Enter number of elements: "))

    if(Size < 0):
        print("Please enter a valid input")
        return
    
    Numbers = []

    print("Enter numbers : ")
    for i in range(Size):
        no = int(input())
        Numbers.append(no)

    Res = Addition(Numbers)

    print("Addition of numbers is : ",Res)


if __name__ == "__main__":
    main()