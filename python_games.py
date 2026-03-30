import random

# --- Game 1: Guessing Game ---
def guessing_game():
    """Guess a number between 1 and 10."""
    number = random.randint(1, 10)
    guess = int(input("Guess 1-10: "))
    if guess == number:
        print("Correct!")
    else:
        print(f"Wrong! It was {number}")
# --- Game 2: Rock, Paper, Scissors ---
def rps_game():
    """Play rock, paper, scissors against the computer."""
    choices = ['rock', 'paper', 'scissors']
    user = input("rock, paper, or scissors? ").lower()
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")
    if user == comp:
        print("Tie!")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print("You win!")
    else:
        print("You lose!")
# --- Game 3: Number Guessing with Hints ---
def guessing_hints_game():
    """Guess a number between 1 and 20 with hints."""
    number = random.randint(1, 20)
    while True:
        guess = int(input("Guess 1-20: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! It was {number}")
            break
# --- Main Menu ---
def main():
    """Choose a game to play."""
    print("Python Games: 1-Guess, 2-RPS, 3-Guess+Hints")
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        guessing_game()
    elif choice == '2':
        rps_game()
    elif choice == '3':
        guessing_hints_game()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
print("git and github learning")
print("this is a new feature branch")





exit()
