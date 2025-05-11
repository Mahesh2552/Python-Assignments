def IsDivisibleBy5(n):
    """
    This function checks if a number is divisible by 5.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is divisible by 5, False otherwise.
    """
    return n % 5 == 0

if __name__ == "__main__":
   
   print("Enter a number:")
   no = int(input())
   if IsDivisibleBy5(no):
       print("The number is divisible by 5")
   else:
       print("The number is not divisible by 5")
    