bids = {}
def winner_bidder(bidder_dict):
    winner = ""
    highest_bidder = 0
    for bidder in bidder_dict:
        bid_amount = bidder_dict[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder


    print(f"The winner is {winner} with a bid price of {highest_bidder}")

while True:
    u_name = input("Enter your name: ")
    u_bid_price = int(input("What is your bid price: "))
    bids[u_name] = u_bid_price

    new_bid = input("Is there a new bid?: (Y/N)")

    if new_bid == "Y":
        continue
    elif new_bid == "N":
        winner_bidder(bids)
        break
    else:
        print("Invalid input")

