"""
Program: Mad Libs Game
------------------------------
Prompts the user for an adjective, a noun, and a verb,
then constructs a fun sentence using their inputs.
"""

# Sentence starter constant
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    """Prompts the user for words and prints a fun sentence."""
    # Get user input
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct and display the final sentence
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
