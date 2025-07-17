import random
import art
from game_data import data


def check_answer(choice, followers_a, followers_b, score):
    if choice == 'a' and followers_a > followers_b:
        score += 1
    elif choice == 'b' and followers_b > followers_a:
        score += 1
    else:
        score = 0
        print("Sorry, that's wrong. Final score is 0")
    return score


# Choose 2 items randomly from the data list to compare
choice_a = random.choice(data)
choice_b = random.choice(data)

follower_count_a = choice_a['follower_count']
follower_count_b = choice_b['follower_count']

print(art.logo)
# Display both with "vs"" and game logo
print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
print(art.versus)
print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

score = 0

# Compare follower counts; if player is wrong, game over; if player is right, add 1 to score, item B becomes A, find new B
player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

score = check_answer(player_choice, follower_count_a, follower_count_b, score)

    

# Compare both items again