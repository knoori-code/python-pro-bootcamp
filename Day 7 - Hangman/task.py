import random

lives = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
correct_letters = []

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

while not game_over:
    guess = input("Guess a letter:\n").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        game_over = True
        print("You win!")
    print(display)