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

# Create function to tally scores
def final_game_scores(who, hand, total):
    print(f"{who} final hand: {hand}, final score: {total}")

player_score = sum(player_cards)
computer_score = sum(computer_cards)

print(f"Your cards: {player_cards}, current score: {player_score}")
print(f"Computer's first card: {computer_cards[0]}")

# Check if Blackjack achieved
if player_score == 21 and computer_score == 21:
    final_game_scores('Your', player_cards, player_score)
    final_game_scores('Computer\'s', computer_cards, computer_score)
    print("The game is a tie with double Blackjack!")

want_another_card = input("Type 'y' to get another card, type 'n' to pass: ")