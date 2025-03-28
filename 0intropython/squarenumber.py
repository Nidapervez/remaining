def main():
    # Prompt the user for a number
    num = float(input("Type a number to see its square: "))

    # Calculate the square
    square = num ** 2

    # Print the result using an f-string
    print(f"{num} squared is {square}")

# Required line to call the main function
if __name__ == '__main__':
    main()
