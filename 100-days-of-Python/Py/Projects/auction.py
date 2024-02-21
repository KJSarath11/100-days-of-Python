bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""

    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount >= highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is the {winner} with the highest bid of {highest_bid}")
    

while not bidding_finished:
    name=input("\nWhat is your name?:")
    price=int(input("What is your bid?:$"))
    bids[name]=price
    should_continue=input("Is there any other bidder?:")

    if should_continue.lower()=="no":
        bidding_finished=True
        find_highest_bidder(bids)
    elif should_continue.lower()=="yes":
        continue