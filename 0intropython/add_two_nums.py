"""
Program: add2numbers
--------------------
This program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Taking input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Calculating the sum
    total = num1 + num2
    
    # Displaying the result
    print("The total is " + str(total) + ".")

# Required to run the program
if __name__ == '__main__':
    main()