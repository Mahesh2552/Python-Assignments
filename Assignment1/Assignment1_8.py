def PrintStars(n):
   # print("* " * n)

    for i in range(1,n+1):
        print("*", end=" ")

if __name__ == "__main__":
    print("Enter the number of stars to print:")
    no = int(input())
    PrintStars(no)
# The function PrintStars takes an integer n as input and prints a line of n stars.