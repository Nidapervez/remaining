"""
Program: Double Each Element in a List
--------------------------------------
Takes a list of numbers and doubles each element.
"""

def double_numbers(numbers: list[int]) -> list[int]:
    """Returns a new list with each element doubled."""
    return [num * 2 for num in numbers]  # Using list comprehension for efficiency

def main():
    """Creates a list of numbers, doubles them, and prints the result."""
    numbers = [1, 2, 3, 4]  # Sample list
    doubled_numbers = double_numbers(numbers)  
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
