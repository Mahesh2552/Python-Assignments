'''
4. Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.

'''

import threading

def SmallCharacters(Str):
    print("Id of small thread: ",threading.get_ident())
    i = 0
    count = 0
    while(i < len(Str)):
        if Str[i].islower():
            count += 1
        i = i + 1
    print("Number of small charactres: ", count,"\n")

def CapitalCharacters(Str):
    print("Id of capital thread: ",threading.get_ident())

    i = 0
    count = 0
    while(i < len(Str)):
        if Str[i].isupper():
            count += 1
        i = i + 1
    print("Number of Capital charactres: ", count,"\n")

def Digits(Str):
    print("Id of digits thread: ",threading.get_ident())

    i = 0
    count = 0
    while(i < len(Str)):
        if Str[i].isdigit():
            count += 1
        i = i + 1
    print("Number of digits : ", count,"\n")

def main():
    Str = input("Enter your string: ")

    small = threading.Thread(target=SmallCharacters, args=(Str,))
    capital = threading.Thread(target=CapitalCharacters, args=(Str,))
    digits = threading.Thread(target=Digits, args=(Str,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    print("End of main")

if __name__ == "__main__":
    main()