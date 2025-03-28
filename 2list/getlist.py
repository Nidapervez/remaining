def main():
    lst = []  # Create an empty list to store values

    val = input("Enter a value: ")  # Get initial input from the user
    while val:  # Continue asking for input until the user presses enter
        lst.append(val)  # Append the entered value to the list
        val = input("Enter a value: ")  # Ask for the next value

    print("Here's the list:", lst)  # Print the final list


# This line ensures that the main function runs when the script is executed
if __name__ == '__main__':
    main()
