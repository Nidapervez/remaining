import time

def countdown_timer(seconds):
    print("\n⏳ Get ready! Countdown starts in...")

    for i in range(3, 0, -1):
        print(f"⏳ {i}...")
        time.sleep(1)

    print("🔥 Countdown Started! 🔥\n")

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        progress = "▓" * (30 * seconds // time_in_seconds) + "░" * (30 - (30 * seconds // time_in_seconds))

        print(f"\r⏲ {mins:02}:{secs:02} [{progress}]", end="")
        time.sleep(1)
        seconds -= 1

    print("\n\n🔔 Time's up! 🔔\a")  # ASCII Bell Sound

# Get valid input from user
while True:
    try:
        time_in_seconds = int(input("⏲ Enter time in seconds: "))
        if time_in_seconds <= 0:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Please enter a valid positive number!")

# Start countdown
countdown_timer(time_in_seconds)
