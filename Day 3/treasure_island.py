print("Welcome to Treasure Island\n")
print("Your mission is to find the treasure\n")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if direction == "right":
    print("You have fallen into a hole. Game Over")
else:
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' for a boat, type 'swim' to swim across.\n").lower()
    if action == "swim":
        print("Attacked by a trout. Game over.")
    else:
        colour = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose?\n").lower()
        if colour == "blue":
            print("Eaten by beasts. Game over.\n")
        elif colour == "red":
            print("Burned by fire. Game over")
        elif colour == "yellow":
            print("You win!")
        else:
            print("Game over!")
