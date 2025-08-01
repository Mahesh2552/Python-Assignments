import os
import sys
import hashlib
import time

def CalculateChecksum(path,block_size = 1024):
    fobj = open(path, 'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(block_size)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(block_size)
    
    fobj.close()

    return hobj.hexdigest()

def duplicate_files(directory_name):
       
    # Check if directory is valid or not
    flag = os.path.isabs(directory_name)
    if (flag == False):
        directory_name = os.path.abspath(directory_name)

    flag = os.path.exists(directory_name)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(directory_name)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(directory_name):

        for fname in FileNames: 
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname) # fname is complete path
            else:
                Duplicate[checksum] = [fname]  #Adding unique files path


    return Duplicate

def duplicate_files_log(duplicate_files):
    Result = list(filter(lambda x : len(x) > 1, duplicate_files.values()))
    
    timestamp = time.ctime()
    filename = "Duplicate%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    obj = open(filename,'x')

    # To store duplicate file names into log file
    for value in Result:
        for subvalue in value:
            obj.write(subvalue+"\n")
        
        obj.write("\n")

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to display the files with given extension")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py DirectorytName")

        else:
            duplicateFiles =duplicate_files(sys.argv[1])
            duplicate_files_log(duplicateFiles)


    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h: Used to display the help")
        print("--u: Used to display the usage")

if __name__ == "__main__":
    main()