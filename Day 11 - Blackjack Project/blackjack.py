import random
import art

# Add a new card to hand
def generate_new_card(whose_cards, deck):
    random_index = random.randint(0, 12)
    whose_cards.append(deck[random_index])


# Generate 2 random cards for computer and player
def complete_computer_hand(hand, deck):
    score = sum(hand)
    while score < 17:
        generate_new_card(hand, deck)
        score = sum(hand)
        while score > 21 and 11 in hand:
            # Change 11 to 1 if total over 21
            index_for_11 = hand.index(11)
            hand[index_for_11] = 1
            score = sum(hand)


def compare_scores(player_sum, computer_sum, player_hand, computer_hand, deck):
    if player_sum == 21 and computer_sum == 21:
        final_game_score('Your', player_hand, player_sum)
        final_game_score('Computer\'s', computer_hand, computer_sum)
        print("The game is a tie with double Blackjack!")
        blackjack()
    
    if player_sum == 21:
        # Tally computer final score
        complete_computer_hand(computer_hand, deck)
        computer_sum = sum(computer_hand)
        final_game_score('Your', player_hand, player_sum)
        final_game_score('Computer\'s', computer_hand, computer_sum)
        print("You win with a Blackjack!")
        blackjack()
    
    if computer_sum == 21:
        final_game_score('Your', player_hand, player_sum)
        final_game_score('Computer\'s', computer_hand, computer_sum)
        print("The computer wins with a Blackjack!")
        blackjack()

    if player_sum > 21:
        final_game_score('Your', player_hand, player_sum)
        final_game_score('Computer\'s', computer_hand, computer_sum)
        print("You went over. You lose!")

    if computer_sum > 21:
        


# Function to tally and show final hands and scores
def final_game_score(who, hand, total):
    print(f"{who} final hand: {hand}, final score: {total}")


def current_game_scores(player_hand, player_total, computer_hand):
    print(f"Your cards: {player_hand}, current score: {player_total}")
    print(f"Computer's first card: {computer_hand[0]}")

def blackjack():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    logo = art.logo
    print(logo)

    player_cards = []
    computer_cards = []

    for i in range(2):
        generate_new_card(player_cards, cards)
        generate_new_card(computer_cards, cards)

    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    current_game_scores(player_cards, player_score, computer_cards)

    # Check if Blackjack achieved
    compare_scores(player_score, computer_score, player_cards, computer_cards, cards)

    want_another_card = True

    while want_another_card:
        card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if card_choice == "y":
            generate_new_card(player_cards, cards)
            player_score = sum(player_cards)
            while player_score > 21 and 11 in player_cards:
                index_position = player_cards.index(11)
                player_cards[index_position] = 1
            current_game_scores(player_cards, player_score, computer_cards)
            # Check game scores and end game if either player or both are over 21

            


blackjack()