# Initial and new prices of futures contracts
initial_prices = {
    "March 2006": 95.25,
    "June 2006": 95.00,
    "September 2006": 94.75
}

new_prices = {
    "March 2006": 94.25,
    "June 2006": 94.00,
    "September 2006": 93.75
}

# Each point in Eurodollar futures represents $25 per basis point per contract
points_per_basis = 25

# Calculate the profit for each contract
paper_profit_march = (initial_prices["March 2006"] - new_prices["March 2006"]) * 100 * points_per_basis
paper_profit_june = (initial_prices["June 2006"] - new_prices["June 2006"]) * 100 * points_per_basis
paper_profit_september = (initial_prices["September 2006"] - new_prices["September 2006"]) * 100 * points_per_basis

# Total paper profit
total_paper_profit = paper_profit_march + paper_profit_june + paper_profit_september

# Results
print(f"The paper profit for the March 2006 contract is ${paper_profit_march:,.2f}.\n")
print(f"The paper profit for the June 2006 contract is ${paper_profit_june:,.2f}.\n")
print(f"The paper profit for the September 2006 contract is ${paper_profit_september:,.2f}.\n")
print(f"The total paper profit is ${total_paper_profit:,.2f}.\n")
