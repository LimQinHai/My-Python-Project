from replit import clear
from ASCII_ART_resource_file import Blind_Auction_logo
print(Blind_Auction_logo)

def find_heighest_bider(auction):
    heighest_price = 0
    winner = ""
    for bidder in auction:
        bidder_price = auction[bidder]
        if bidder_price > heighest_price:
            heighest_price = bidder_price
            winner = bidder

    print(f"The winner is {winner} with a bid of ${heighest_price}.")


terminate = False
auction = {}
while not terminate:

    name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))

    auction[name] = bid_price  #Store name and bid price in a dictionary

    result = input("Is there any other users who want to bid? Type'Yes'or'No'.").lower()

    if result == "yes":
        clear()
    if result == "no":
        terminate = True
        clear()
        find_heighest_bider(auction)