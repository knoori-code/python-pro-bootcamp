height = int(input("What is your height?\n"))

if height >= 120:
    age = int(input("What is your age?\n"))
    if age > 18:
        print("You must pay $12 for the ride")
    elif age >= 12:
        print("The price of the ride is $7")
    else:
        print("You must pay $5")
else:
    print("You are too short to ride the rollercoaster")
