"""
Program: dicesimulator
----------------------
Simulate rolling two dice three times.
Prints the results of each die roll.
This program demonstrates variable scope.
"""

# Import the random module to generate random numbers
import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Total of two dice: {total}")

def main():
    die1 = 10  # Local variable inside main()
    print(f"die1 in main() starts as: {die1}")

    # Roll the dice three times
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"die1 in main() is: {die1}")  # This remains unchanged

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
