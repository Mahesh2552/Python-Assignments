def LengthOfString(string):
    """
    This function takes a string as input and returns its length.
    """
    return len(string)
if __name__ == "__main__":
    print("Enter a string:")
    str1 = input()
    length = LengthOfString(str1)
    print("Length of the string is:", length)