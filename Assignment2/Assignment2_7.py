''' 
7. Write a program which accepts one number and displays below pattern.
   Input : 5
   Output :

   1    2    3    4    5
   1    2    3    4    5
   1    2    3    4    5
   1    2    3    4    5
   1    2    3    4    5
  
'''
def DisplayPattern(Num):
    for i in range(Num):
        for j in range(1, Num+1):
            print(j, end=" ")
        print()


def main():
    No = int(input("Enter a number: "))
    DisplayPattern(No)

if __name__ == "__main__":
    main()
