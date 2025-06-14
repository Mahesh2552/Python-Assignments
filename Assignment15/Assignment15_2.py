import os

def display_file_contains(filename):
   if(os.path.exists(filename)):
      fobj = open(filename, 'r')

      data = fobj.read()

      print(data)

      fobj.close()
   else:
      print(f"{filename} does not exist in the current directory.")

def main():
   fname = input("Enter the file name: ")
   display_file_contains(fname)

if __name__ == "__main__":
   main()

