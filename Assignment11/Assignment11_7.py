'''
7. Print Pattern Using Recursion (Right Triangle)
   Write a recursive function to print the following pattern:

   
   *
   * *
   * * *
   * * * *
   * * * * *
'''

i = 1
def Print_Pattern(n):
   global i

   if i <= n:
      print("* " * i)
      i += 1
      Print_Pattern(n)

def main():
   n = int(input("Enter the number of rows for the pattern: "))
   Print_Pattern(n)  

if __name__ == "__main__":
   main()
