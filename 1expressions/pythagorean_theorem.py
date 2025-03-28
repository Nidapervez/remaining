"""
Program: hypotenuse_calculator
------------------------------
Calculates the hypotenuse of a right triangle using the Pythagorean theorem:
BC² = AB² + AC²
"""

import math  # Import math library to use sqrt function

def main():
    """
    Reads user input for the two perpendicular sides of a right triangle
    and calculates the hypotenuse using the Pythagorean theorem.
    """
    # Get the two side lengths from the user
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse
    bc = math.sqrt(ab**2 + ac**2)

    # Display result
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
