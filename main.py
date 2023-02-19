from replit import clear
from art import logo
print(logo)

# Dictionary function to store bidders
bidders = []

# Function to calculate the highest bidder
def find_highest_bidder(bidders):
    max_bid = 0
    max_name = ""
    for bidder in bidders:
        if bidder["bid"] > max_bid:
            max_bid = bidder["bid"]
            max_name = bidder["name"]
    print(f"The winner is {max_name} with a bid of ${max_bid}")

# Take the initial input from the first bidder
bidders_name = input("What is your name?: ")
bidders_bid = int(input ("What's your bid?: $"))

# Add the first bidder to the bidders list
bidders.append({"name": bidders_name, "bid": bidders_bid})

# Keep asking for new bidders until the answer is 'no'
yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

while yes_or_no == "yes":
    clear()
    bidders_name = input("What is your name?: ")
    bidders_bid = int(input ("What's your bid?: $"))
    bidders.append({"name": bidders_name, "bid": bidders_bid})
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

# Calculate the highest bidder
find_highest_bidder(bidders)
