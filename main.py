from replit import clear
from art import logo
print(logo)
bids = {}
bidding_finished = False

def find_highest_bid(bids):
  highest_bid = 0
  winner = ""
  for bidder in bids:
    bid_amount = bids[bidder]
    if int(bid_amount) > highest_bid: 
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_finished == False:
  name = input("What is your name? ")
  amount = input("What is your bid? $")
  bids[name] = amount
  one_more = input("Any other who wants to bid? Yes or No?\n").lower()
  if one_more == "no":
    bidding_finished = True
    find_highest_bid(bids)
  elif one_more == "yes":
    clear()
