import os
import sys

def copy_file_contents(old_file, new_file):
    
   if not os.path.exists(old_file):
      print(f"{old_file} does not exist in the current directory.")
      exit()

   fobj = open(old_file, 'r')
   data = fobj.read()
   fobj.close()

   fobj = open(new_file, 'w')
   fobj.write(data)
   fobj.close()

   print(f"Contents of {old_file} copied to {new_file} successfully.")

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to copy file contents to a new file")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py FileName")

      else:
         copy_file_contents(sys.argv[1],"Demo.txt")

   else:
      print("Invalid number of command line arguments")
      print("Use the given flags as :")
      print("--h: Used to display the help")
      print("--u: Used to display the usage")

if __name__ == "__main__":
   main()


