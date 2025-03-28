"""
Program: division_calculator
------------------------------
Asks the user for two integers, divides them, and prints 
both the quotient and the remainder.
"""

def main():
    """
    Reads two integers from the user and calculates
    the quotient and remainder.
    """
    # Get user input
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform integer division and get remainder
    quotient = dividend // divisor  
    remainder = dividend % divisor  

    # Display result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
