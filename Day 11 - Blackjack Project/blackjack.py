import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

begin_game = input("Do you want to play a game of blackjack? type 'y' or 'no': ")

player_cards = []
computer_cards = []

def generate_random_card():
    index = random.randint(0, 12)
    random_card = cards[index]
    return random_card