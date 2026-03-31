import random

print("🎲 Welcome to Roll the Dice!")

while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    
    if roll == "yes":
        dice = random.randint(1, 6)
        print("You rolled:", dice)
    elif roll == "no":
        print("Thanks for playing!")
        break
    else:
        print("Type 'yes' or 'no'")
        import random

# Choose a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10. Can you guess it?")

# Give the player 3 tries
for tries in range(3):
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print("Sorry! You ran out of tries.The number was", secret_number)
    score = 0

print("Welcome to the True/False Game!")

answer1 = input("Python is a snake? (True/False): ")

if answer1 == "False":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer2 = input("5 > 2 ? (True/False): ")

if answer2 == "True":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score is:", score)
