def main():
    # Define ages based on the given conditions
    anton = 21  # Anton's age is 21
    beth = anton + 6  # Beth is 6 years older than Anton
    chen = beth + 20  # Chen is 20 years older than Beth
    drew = chen + anton  # Drew is as old as Chen's age plus Anton's age
    ethan = chen  # Ethan is the same age as Chen

    # Print the results
    print("Anton is", anton)
    print("Beth is", beth)
    print("Chen is", chen)
    print("Drew is", drew)
    print("Ethan is", ethan)

# Required line to call the main function
if __name__ == '__main__':
    main()
