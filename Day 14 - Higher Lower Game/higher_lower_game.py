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

# Compare follower counts; if player is wrong, game over; if player is right, add 1 to score, item B becomes A, find new B

# Compare both items again