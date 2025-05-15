def PrintStar(rows):
    
    for i in range(rows):
        for j in range(i+1):
            print("* ", end="")
        print()
        

def main():
   num_of_rows = int(input("Enter number of rows of * you want: "))

   PrintStar(num_of_rows)

if __name__ == "__main__":
    main()