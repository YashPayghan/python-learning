#TODO-1: Ask the user for input
name=input("what is your name?\n")
bid=input("what is your bid?\n")
# TODO-2: Save data into dictionary {name: price}
bidding= {name: bid}
other=input("is there any other bideer?(yes/no)\n").lower()
while other=="yes":
    print("\n"*10)
    name = input("what is your name?\n")
    bid = input("what is your bid?\n")
    bidding[name]=bid
    other = input("is there any other bideer?(yes/no)\n").lower()
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
print("\n"*10)
def highest_bidder():
    highest_bid="0"
    for bider in bidding:
        bid=bidding[bider]
        if bid > highest_bid:
            highest_bid=bid

    print ("the winnner of the auction is",bider,"with the highest bid of",highest_bid)

highest_bidder()