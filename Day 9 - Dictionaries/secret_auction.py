continue_auction = True
auction_dictionary = {}

while continue_auction:

    name = input("What is your name?: ")
    bid = input("What is your bid?: $")

    auction_dictionary[name] = bid

    continue_response = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_response == 'no':
        continue_auction = False

for key in auction_dictionary:
    