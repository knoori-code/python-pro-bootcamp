continue_auction = True
auction_dictionary = {}

while continue_auction:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    auction_dictionary[name] = bid

    continue_response = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_response == 'no':
        continue_auction = False

max_bid = 0
for key in auction_dictionary:
    if auction_dictionary[key] > max_bid:
        max_bid = auction_dictionary[key]
        name = key

print(f"The winner is {name} with a bid of ${max_bid}!")