import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': "))
number = random.randint(1, 100)
print(f"The secret number is {number}")

attempts_dict = {
    "easy": 10,
    "hard": 5
}

if difficulty == 'easy':
    attempts = attempts_dict["easy"]
else:
    attempts = attempts_dict["hard"]

continue_guessing = True
while continue_guessing:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > number:
        print("Too high.\nGuess again.")
        attempts -= 1
    elif guess < number:
        print(f"Too low.\nGuess again.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
        continue_guessing = False

    if attempts == 0:
        print(f"You've run out of guesses. Game over.")
        continue_guessing = False