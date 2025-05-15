def main():
    char = input("Enter a character: ")
    if len(char) != 1:
        print("Please enter a single character.")
        return
    
    if not char.isalpha():
        print("Please enter a valid alphabetic character.")
        return
        
    if char == "a" or char =="e" or char == "i" or char == "o" or char == "u":
        print("The character is a vowel.")
    elif char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")

if __name__ == "__main__":
    main()