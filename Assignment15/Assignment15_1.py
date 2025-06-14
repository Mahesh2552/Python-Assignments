import os

def check_file_exists(filename):

   return (os.path.exists(filename))


def main():
   fname = input("Enter the file name to check if is exists:")

   ret = check_file_exists(fname)

   if ret == True:
      print(f"{fname} exists in the current directory.")
   else:
      print(f"{fname} does not exist in the current directory.")

if __name__ == "__main__":
   main()

