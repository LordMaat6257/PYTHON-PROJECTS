import random
DIFFICULTY_SETTINGS = {
    "easy":     {"low": 1,   "high": 10,  "max_attempts": 6, "multiplier": 1},
    "medium":   {"low": 1,   "high": 50,  "max_attempts": 5, "multiplier": 2},
    "difficult":{"low": 1,   "high": 100, "max_attempts": 4, "multiplier": 3},
}
def print_intro():
    print("""Welcome to the Number Guessing Game!
How it works:
    - Choose a difficulty level: Easy, Medium, or Difficult.")
    - I will pick a secret number in a range based on your choice.")
    - You have limited attempts to guess it.")
    - After each guess, I’ll tell you: Too low, Too high, or Correct!")
    - If you guess correctly in time, you score points based on speed and level.\n""")
def choose_difficulty():
    while True:
        choice = input("Choose level: easy / medium / difficult → ").strip().lower()
        if choice in DIFFICULTY_SETTINGS:
            return choice
        print("Invalid choice. Please type 'easy', 'medium', or 'difficult'.")
def get_valid_int(prompt, low, high):
    """Ask for an integer within [low, high]. Re-prompt on invalid input."""
    while True:
        raw = input(prompt).strip()
        if not raw.lstrip("-").isdigit():
            print("Please enter a valid whole number.")
            continue
        value = int(raw)
        if value < low or value > high:
            print(f"Out of range. Enter a number between {low} and {high}.")
            continue
        return value
def play_round(level_name):
    cfg = DIFFICULTY_SETTINGS[level_name]
    low, high = cfg["low"], cfg["high"]
    max_attempts = cfg["max_attempts"]
    multiplier = cfg["multiplier"]
    secret = random.randint(low, high)
    print(f"\nI have chosen a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts to guess it.")
    for attempt in range(1, max_attempts + 1):
        guess = get_valid_int(f"\nEnter your guess ({low}-{high}): ", low, high)
        if guess < secret:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Too low! Attempts left: {remaining}")
            else:
                print("Too low!")
        elif guess > secret:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Too high! Attempts left: {remaining}")
            else:
                print("Too high!")
        else:
            base_score = (max_attempts - attempt + 1)
            final_score = base_score * multiplier
            print(f"\n Correct! You guessed it in {attempt} attempt{'s' if attempt != 1 else ''}!")
            print(f"Your final score = ({max_attempts} - {attempt} + 1) × {multiplier} = {final_score}\n")
            return
    print("\nGame Over! You ran out of attempts.")
    print(f"The correct number was: {secret}")
    print("Your final score = 0\n")
def play_again():
    while True:
        ans = input("Play again? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")
def main():
    print_intro()
    while True:
        level = choose_difficulty()
        play_round(level)
        if not play_again():
            print("\nThanks for playing! See you next time.")
            break
if __name__ == "__main__":
    main()
