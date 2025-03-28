import random

def play_game():
    print("\n🎮 Welcome to Rock, Paper, Scissors! ✂️🪨📄")
    print("🔹 Type 'rock', 'paper', or 'scissors' to play.")
    print("🔹 Type 'exit' anytime to quit the game.\n")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("🤔 Choose: Rock, Paper, or Scissors? ").strip().lower()

        if user_choice == "exit":
            print("👋 Thanks for playing! See you next time. 🎭")
            break

        if user_choice not in choices:
            print("⚠️ Invalid choice! Please choose Rock, Paper, or Scissors. ❌\n")
            continue

        computer_choice = random.choice(choices)

        print(f"\n🧑 You chose: {user_choice.capitalize()} 🎭")
        print(f"🤖 Computer chose: {computer_choice.capitalize()} 💻")

        if user_choice == computer_choice:
            print("😲 It's a tie! Try again. 🔄\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win! 🏆🔥\n")
        else:
            print("😢 You lose! Better luck next time. 💀\n")

# Start the game
play_game()