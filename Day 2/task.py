print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15\n"))
total_with_tip = total_bill * (tip_amount/100 + 1)
number_of_people = int(input("How many people to split the bill?\n"))
amount_per_person = total_with_tip/number_of_people
rounded_amount = round(amount_per_person, 2)

print(f"Each person should pay {rounded_amount}")