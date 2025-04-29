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
        if score > 21 and 11 in hand:
            # Change 11 to 1 if total over 21
            index_for_11 = hand.index(11)
            hand[index_for_11] = 1
            score = sum(hand)


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
    if player_score == 21 and computer_score == 21:
        final_game_score('Your', player_cards, player_score)
        final_game_score('Computer\'s', computer_cards, computer_score)
        print("The game is a tie with double Blackjack!")
        blackjack()
    
    if player_score == 21:
        # Tally computer final score
        complete_computer_hand(computer_cards, cards)
        computer_score = sum(computer_cards)
        final_game_score('Your', player_cards, player_score)
        final_game_score('Computer\'s', computer_cards, computer_score)
        print("You win with a Blackjack!")
        blackjack()
    
    if computer_score == 21:
        final_game_score('Your', player_cards, player_score)
        final_game_score('Computer\'s', computer_cards, computer_score)
        print("The computer wins with a Blackjack!")
        blackjack()

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
            # Check if player is over 21. End game if they are


blackjack()