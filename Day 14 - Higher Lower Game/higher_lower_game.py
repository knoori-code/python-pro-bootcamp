import random
import art
from game_data import data

# Choose 2 items randomly from the data list to compare
choice_a = random.choice(data)
choice_b = random.choice(data)

print(art.logo)
# Display both with "vs"" and game logo
print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
print(art.versus)
print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

score = 0
# Compare follower counts; if player is wrong, game over; if player is right, add 1 to score, item B becomes A, find new B
player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

follower_count_a = choice_a['follower_count']
follower_count_b = choice_b['follower_count']

if player_choice == 'a' and follower_count_a > follower_count_b:
    score += 1
    choice_a = choice_b
elif player_choice == 'a' and follower_count_a < follower_count_b:
    score = 0
    print("Sorry, that's wrong. Final score is {score}")
elif player_choice == 'b' and follower_count_b > follower_count_a:
    score += 1
    choice_a = choice_b
elif player_choice == 'b' and follower_count_b < follower_count_a:
    print("Sorry, that's wrong. Final score is {score}")
    

# Compare both items again