import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
correct_letters = []

for letter in chosen_word:
    placeholder += "_"


lives = 6
stages_index = -1
game_over = False

while not game_over:
    print(f"Word to guess: {placeholder}")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if guess not in display:
        lives -= 1
        stages_index -= 1
    
    placeholder = display
    print(display)
    print(stages[stages_index])
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    if lives == 0:
        game_over = True
        print("You lose!")
    
    if "_" not in display:
        game_over = True
        print("You win!")