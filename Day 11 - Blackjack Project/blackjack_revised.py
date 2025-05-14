import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(): 
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    player_hand = []
    computer_hand = []

    if play_game == 'y':
        print(art.logo)

        for i in range(2):
            # Add cards to player and computer cards