import art
print(art.logo)
print("Welcome to the silent auction!")
bids = {}
bidding = True
while bidding:
    name = input("What is your name?\n").lower()
    bid = int(input("What is your bid? $"))
    bids[bid] = name
    reset = input("Continue bidding? Y or N\n").lower()
    if reset == "y":
        print("\n" * 20)
        continue
    else:
        highest_bid = max(bids)
        winner = bids[max(bids)]
        print(f"Auction over! {winner} wins with a bid of {highest_bid}")
        bidding = False