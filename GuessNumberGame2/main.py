import random
import time
from colorama import Fore, Style

def guess_the_number():
    print(Fore.YELLOW + "🎯 Welcome to the 'Guess the Number' Game! 🤩🎮" + Style.RESET_ALL)
    print(Fore.GREEN + "🤖 The computer has chosen a secret number. Can you guess it? 🔢🤔\n" + Style.RESET_ALL)

    while True:
        # Difficulty selection
        print(Fore.CYAN + "Choose your difficulty level:" + Style.RESET_ALL)
        print("1️⃣ Easy (1-10, Unlimited Attempts)")
        print("2️⃣ Medium (1-20, 5 Attempts)")
        print("3️⃣ Hard (1-50, 7 Attempts)")

        difficulty = input(Fore.MAGENTA + "Enter 1, 2, or 3: " + Style.RESET_ALL)

        if difficulty == "1":
            max_number = 10
            max_attempts = None  # Unlimited attempts
        elif difficulty == "2":
            max_number = 20
            max_attempts = 5
        elif difficulty == "3":
            max_number = 50
            max_attempts = 7
        else:
            print(Fore.RED + "⚠️ Invalid choice! Please enter 1, 2, or 3." + Style.RESET_ALL)
            continue

        # Generate random secret number
        secret_number = random.randint(1, max_number)
        attempts = 0  # Track attempts

        print(Fore.BLUE + f"\n🔍 The secret number is between **1 and {max_number}**. Start guessing!" + Style.RESET_ALL)

        while True:
            try:
                user_guess = int(input(Fore.YELLOW + "💡 Enter your guess: " + Style.RESET_ALL))
                attempts += 1

                # Check the guess
                if user_guess < 1 or user_guess > max_number:
                    print(Fore.RED + f"⚠️ Please guess within the range **1 to {max_number}**!" + Style.RESET_ALL)
                    continue

                if user_guess < secret_number:
                    hint = "📉 Too low! " + ("You're getting closer! 🔥" if secret_number - user_guess <= 3 else "Try a higher number! ⬆️")
                    print(Fore.RED + hint + Style.RESET_ALL)
                elif user_guess > secret_number:
                    hint = "📈 Too high! " + ("Almost there! 🌟" if user_guess - secret_number <= 3 else "Try a lower number! ⬇️")
                    print(Fore.RED + hint + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + f"🎉 **Congratulations!** 🎊 You guessed the right number in **{attempts}** attempts! 🏆🥳" + Style.RESET_ALL)
                    break

                # Check attempt limit
                if max_attempts and attempts >= max_attempts:
                    print(Fore.RED + f"❌ You've used all {max_attempts} attempts! The number was {secret_number}. Better luck next time! 😢" + Style.RESET_ALL)
                    break

            except ValueError:
                print(Fore.RED + "⚠️ **Oops!** Please enter a valid **number**!" + Style.RESET_ALL)

        # Play again option
        play_again = input(Fore.CYAN + "\n🔄 Do you want to play again? (yes/no): " + Style.RESET_ALL).strip().lower()
        if play_again != 'yes':
            print(Fore.YELLOW + "🎮 Thanks for playing! See you next time! 👋😊" + Style.RESET_ALL)
            break

# Run the game
guess_the_number()