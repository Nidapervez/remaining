def main():
    curr_value = int(input("Enter a number: "))  # Get user input

    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print result in a single line

# Required line to call the main() function
if __name__ == '__main__':
    main()
