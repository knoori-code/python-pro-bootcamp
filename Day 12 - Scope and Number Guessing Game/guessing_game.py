print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts_dict = {
    "easy": 10,
    "hard": 5
}

if difficulty == 'easy':
    attempts = attempts_dict["easy"]
else:
    attempts = attempts_dict["hard"]



