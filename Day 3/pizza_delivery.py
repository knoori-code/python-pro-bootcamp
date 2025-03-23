print("Welcome to Python Pizza deliveries")
size = input("What size of pizza do you want? S, M, or L: \n").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").lower()

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your bill is {bill}")