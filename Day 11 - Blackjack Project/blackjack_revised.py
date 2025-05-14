import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generate_random_card(hand):
    random_index = random.randint(0, 12)
    hand.append(cards[random_index])

def blackjack(): 
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    player_hand = []
    computer_hand = []

    if play_game == 'y':
        print(art.logo)

        # Generate 2 cards for each player
        for i in range(2):
            generate_random_card(player_hand)
            generate_random_card(computer_hand)