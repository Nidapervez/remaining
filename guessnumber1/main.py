import random

def computer_guess():
    print("\n🎯 Welcome to the 'Guess the Number' Game! 🤖🎲")
    print("🤔 Think of a number between **1 and 20**, and I'll try to guess it! 🔢")
    print("🔹 After each guess, type:")
    print("   - 'H' if my guess is too **High** ⬆️")
    print("   - 'L' if my guess is too **Low** ⬇️")
    print("   - 'C' if I guessed **Correctly** ✅\n")

    low, high = 1, 20
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1

        print(f"\n🤖 My guess is: **{guess}** 🎯")
        feedback = input("📢 Is it (H)igh, (L)ow, or (C)orrect? ").strip().lower()

        if feedback == "c":
            print(f"\n🎉 Wohoooo! 🥳 I guessed your number in **{attempts}** attempts! 🏆🔥")
            break
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("⚠️ **Invalid input!** Please enter 'H' for High, 'L' for Low, or 'C' for Correct.")

    else:
        print("\n⚠️ Something went wrong! Did you change your number? 😲")

# Start the game
computer_guess()