import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

logo = art.logo
print(logo)

player_cards = []
computer_cards = []

# Generate 2 random cards for computer and player
for i in range(2):
    random_index1 = random.randint(0, 12)
    random_index2 = random.randint(0, 12)
    player_cards.append(cards[random_index1])
    computer_cards.append(cards[random_index2])

player_score = sum(player_cards)

print(f"Your cards: {player_cards}, current score: {player_score}")
print(f"Computer's first card: {computer_cards[0]}")