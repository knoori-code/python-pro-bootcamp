import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generate_random_card(hand):
    random_index = random.randint(0, 12)
    hand.append(cards[random_index])


def show_current_score(player_cards, computer_cards):
    player_score = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")


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

        # Show player's current cards and score and computer's first card
        show_current_score(player_hand, computer_hand)

        # Check if either player has blackjack. End game and declare winner if they do
        player_score = sum(player_hand)
        computer_score = sum(computer_hand)

        if player_score == 21 and computer_score == 21:
            print("Both players have Blackjack! The game is a draw.")
            blackjack()

        if player_score == 21:
            print("You win the game with a Blackjack!")
            blackjack()

        if computer_score == 21:
            print("The computer has Blackjack! You lose.")

        


blackjack()