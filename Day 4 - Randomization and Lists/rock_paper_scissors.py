import random

game_symbols = ["Rock", "Paper", "Scissors"]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
if player_choice >= 0 and player_choice <= 2:  
    print(game_symbols[player_choice])
print("Computer chose:")
print(game_symbols[computer_choice])

if player_choice > 2 or player_choice < 0:
    print("You chose an invalid number. You lose!")
elif player_choice == computer_choice:
    print("You both chose the same thing. It's a tie!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
elif computer_choice > player_choice:
    print("You lose!")