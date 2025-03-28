"""
Program: feet_to_inches_converter
---------------------------------
Converts feet to inches. 
There are 12 inches per foot.
"""

# Define conversion factor
INCHES_IN_FOOT = 12  

def main():
    """
    Reads user input in feet and converts it to inches.
    """
    # Get input from the user
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT

    # Display result
    print(f"That is {inches} inches!")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
