"""
Program: Sum of Numbers in a List
---------------------------------
Takes a list of numbers and returns the sum.
"""

def add_many_numbers(numbers: list[int]) -> int:
    """Takes in a list of numbers and returns their sum."""
    return sum(numbers)  # Using Python's built-in sum function for simplicity

def main():
    """Creates a list of numbers, computes the sum, and prints it."""
    numbers = [1, 2, 3, 4, 5]  # Sample list of numbers
    sum_of_numbers = add_many_numbers(numbers)
    print(f"The sum of {numbers} is {sum_of_numbers}")  # Enhanced output formatting

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
