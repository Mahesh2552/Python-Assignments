import os

def check_file_exists(filename):

   return (os.path.exists(filename))

def main():

   fname = input("Enter name of the file: ")
   ret = check_file_exists(fname)

   if(ret == True):
      print(f"{fname} file exists in the current directory.")
   else:
      print(f"{fname} file does not exists in the current directory.")

if __name__ == "__main__":
   main()

