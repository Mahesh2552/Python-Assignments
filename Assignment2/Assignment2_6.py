''' 
6. Write a program which accepts one number and displays below pattern.
   Input : 5
   Output :

  
   *       *       *       *       *
   *       *       *       * 
   *       *       * 
   *       * 
   * 
   

'''

def PrintStar(rows):
   for i in range(rows,0,-1):
      j = i
      while(j > 0):
         print("* ", end="")
         j -= 1
      print()   
      
# for i in range(rows,0,-1):
#     print("* " * i)

def main():
   num_of_rows = int(input("Enter number of rows of * you want: "))

   if(num_of_rows>0):
      PrintStar(num_of_rows)
   else:
      print("Please enter value greater than 0")

if __name__ == "__main__":
   main()
