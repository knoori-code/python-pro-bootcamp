import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# begin_game = input("Do you want to play a game of blackjack? type 'y' or 'no': ")


def check_score(card_list):
    total = sum(card_list)
    return total

def generate_random_card():
    index = random.randint(0, 12)
    random_card = cards[index]
    return random_card

question = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
player_cards = []
computer_cards = []

for i in range(2):
    player_cards.append(generate_random_card())
    computer_cards.append(generate_random_card())

computer_first_card = computer_cards[0]

print(f"Your cards: {player_cards}, current score: {check_score(player_cards)}")
print(f"Computer's first card: {computer_first_card}")

another_card_choice = input("Type 'y' to get another card, type 'n' to pass: ")

if another_card_choice == 'y':
    player_cards.append(generate_random_card())
