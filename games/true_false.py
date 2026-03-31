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
