import psutil

def ProcessDisplay():
    Border = "*"*64
    print(Border)
    print("Information of currently running processes:")
    print(Border)
    
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        info['vms'] = proc.memory_info().vms / (1024 * 10124)
        print(info)

def main():
    ProcessDisplay()

if __name__ == "__main__":
    main()