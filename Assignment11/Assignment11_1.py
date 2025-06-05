'''
1. Print Numbers Using Recursion
   Write a recursive function to print numbers from 1 to N.
   Expected Output (for n=5):
   1 2 3 4 5
'''
i = 1

def PrintNumbers(num):
   global i
   
   if i <= 5:
      print(i, end = " ")
      i += 1
      PrintNumbers(num)
   else:
      return

def main():
   num = 5
   PrintNumbers(num)

if __name__ == "__main__": 
   main()