import random

N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1   # Minimum range value
MAX_VALUE: int = 100 # Maximum range value

def main():
    # Generate and print 10 random numbers in the range 1 to 100
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    print()  # Newline after printing all numbers

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
