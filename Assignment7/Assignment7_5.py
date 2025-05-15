def IsPalindrome(Str):
    i = 0
    while(i <= (len(Str))/2):
        if Str[i] != Str[len(Str) - i - 1]:
            return False
        i += 1
    
    return True

# return (Str == Str[::-1])

def main():
    String = input("Enter string: ")

    if IsPalindrome(String):
        print(String, " is a palindrome.")
    else:
        print(String, " is not a ppalindrome.")

if __name__ == "__main__":
    main()