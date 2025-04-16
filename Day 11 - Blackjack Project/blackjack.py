import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# begin_game = input("Do you want to play a game of blackjack? type 'y' or 'no': ")

player_cards = []
computer_cards = []

def generate_random_card():
    index = random.randint(0, 12)
    random_card = cards[index]
    return random_card

# generate 2 cards for the player and computer
for i in range(2):
    player_cards.append(generate_random_card())
    computer_cards.append(generate_random_card())

# print(player_cards, computer_cards)