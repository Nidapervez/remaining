"""
Program: dice_roller
------------------------------
Simulates rolling two dice, prints the results of each roll, 
and displays their total.
"""

import random  # Import the random module for simulating dice rolls

# Define the number of sides on each die
NUM_SIDES = 6  

def roll_dice():
    """Rolls a single die and returns the result."""
    return random.randint(1, NUM_SIDES)

def main():
    """
    Simulates rolling two dice, prints each roll, 
    and calculates the total.
    """
    # Roll two dice
    die1 = roll_dice()
    die2 = roll_dice()
    
    # Compute the total
    total = die1 + die2
    
    # Display results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
