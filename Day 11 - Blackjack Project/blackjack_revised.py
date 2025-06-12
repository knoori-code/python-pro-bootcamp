import art
import random


def generate_random_card(hand):
    random_index = random.randint(0, 12)
    hand.append(cards[random_index])


def show_current_score(player_cards, computer_cards):
    player_score = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")


def show_final_scores(player_cards, computer_cards):
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(): 
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
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

        # Check if either player has Blackjack
        player_score = sum(player_hand)
        computer_score = sum(computer_hand)

        if player_score == 21:
            player_score = 0

        if computer_score == 21:
            computer_score = 0

        if player_score == 0 and computer_score == 0:
            # Show final scores
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            # print message saying who won
            print("Both players have Blackjack! The game is a draw.")
            # Restart blackjack function by calling it again
            blackjack()

        if player_score == 0:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("You win with a Blackjack!")
            blackjack()

        if computer_score == 0:
            print(f"Your final hand: {player_hand}, final score: {player_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("The computer has Blackjack. You lose.")
            blackjack()

        
        want_another_card = True
        while want_another_card:
            card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            # if want another card, add card to player's hand
            if card_choice == 'y':
                generate_random_card(player_hand)
                player_score = sum(player_hand)

                # While player score > 21 and 11s in hand, change to 1
                while player_score > 21 and 11 in player_hand:
                    index_position = player_hand.index(11)
                    player_hand[index_position] = 1
                    show_current_score(player_hand, computer_hand)
                elif player_score > 21:
                    show_current_score(player_hand, computer_hand)
                    show_final_scores(player_hand, computer_hand)
                    print("You went over 21. You lose!")

                

            # else:
                # if player doesn't want card, tally scores and determine winner

        


blackjack()