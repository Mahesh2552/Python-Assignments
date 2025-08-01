import sys
import psutil

def DisplayProcessInformation(process_name):
    try:
        flag = False
        # To check if the process is running and display its information
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                info = proc.as_dict(attrs=['pid', 'name', 'username'])
                info['vms'] = proc.memory_info().vms / (1024 * 1024)
                print(info)
                flag = True
                print(f"Process '{process_name}' is running.")
        if not flag:
            print(f"Process '{process_name}' is not running.")
    
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
        print(f"Error accessing process information: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to display the files with given extension")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py ProcessName")

        else:
            DisplayProcessInformation(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h: Used to display the help")
        print("--u: Used to display the usage")

if __name__ == "__main__":
    main()