height = int(input("What is your height?\n"))

if height >= 120:
    age = int(input("What is your age?\n"))
    if age > 18:
        bill = 12
        print("The ride is $12")
    elif age >= 12:
        bill = 7
        print("The ride is $7")
    else:
        print("the ride is $5")
        bill = 5

    want_photo = input("Would you like a photo?\n")
    if want_photo == "y":
        bill += 3

    print(f"Your bill is {bill}")

else:
    print("You are too short to ride the rollercoaster")