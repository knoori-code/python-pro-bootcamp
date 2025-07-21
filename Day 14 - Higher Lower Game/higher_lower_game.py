import random
import art
from game_data import data


def check_answer(choice, followers_a, followers_b, score):
    if choice == 'a' and followers_a > followers_b:
        score += 1
    elif choice == 'b' and followers_b > followers_a:
        score += 1
    else:
        print("\n" * 5)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score is {score}")
        score = 0
    return score


def higher_lower_game():
    score = 0
    # Choose 2 items randomly from the data list to compare
    choice_a = random.choice(data)
    choice_b = random.choice(data)

    guessed_correct = True

    while guessed_correct:
        print(art.logo)
        follower_count_a = choice_a['follower_count']
        follower_count_b = choice_b['follower_count']

        # Display both with "vs"" and game logo
        if score > 0:
            print(f"You're right! Current score: {score}")

        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(art.versus)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

        # Compare follower counts; if player is wrong, game over; if player is right, add 1 to score, item B becomes A, find new B
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        score = check_answer(player_choice, follower_count_a, follower_count_b, score)

        if score > 0:
            choice_a = choice_b
            choice_b = random.choice(data)
        else:
            guessed_correct = False


higher_lower_game()