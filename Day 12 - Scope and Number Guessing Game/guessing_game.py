import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 100)

attempts_dict = {
    "easy": 10,
    "hard": 5
}

if difficulty == 'easy':
    attempts = attempts_dict["easy"]
else:
    attempts = attempts_dict["hard"]

print(f"You have {attempts} attempts remaining to guess the number.")

guess = input("Make a guess: ")

if guess > number:
    print("Too high.\nGuess again.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
elif guess < number:
    print(f"Too low.\nGuess again.")
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    print("You got it! The answer was {number}.")
    