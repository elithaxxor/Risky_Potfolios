# Define initial values
initial_contracts = 25
price_initial = 1223
price_july12 = 1243
price_july13 = 1273
price_july14 = 1293
price_july15 = 1343
ounces_per_contract = 100

# [USER INPUT] Define the initial values
# Day 1: July 12
profit_july12 = (price_july12 - price_initial) * initial_contracts * ounces_per_contract
total_contracts_july13 = 50 # Buy 25 more contracts, total contracts = 50

# Day 2: July 13
profit_july13 = (price_july13 - price_july12) * total_contracts_july13 * ounces_per_contract
total_contracts_july14 = 125 # Buy 75 more contracts, total contracts = 125

# Day 3: July 14
profit_july14 = (price_july14 - price_july13) * total_contracts_july14 * ounces_per_contract
total_contracts_july15 = 250 # Buy 125 more contracts, total contracts = 250

# Day 4: July 15
profit_july15 = (price_july15 - price_july14) * total_contracts_july15 * ounces_per_contract

# Break down the final day profits for different contract blocks
profit_25_contracts_initial = (price_july15 - price_initial) * initial_contracts * ounces_per_contract
profit_25_contracts_july12 = (price_july15 - price_july12) * initial_contracts * ounces_per_contract
profit_75_contracts_july13 = (price_july15 - price_july13) * 75 * ounces_per_contract
profit_125_contracts_july14 = (price_july15 - price_july14) * 125 * ounces_per_contract

# Total profit
total_profit = (
    profit_25_contracts_initial +
    profit_25_contracts_july12 +
    profit_75_contracts_july13 +
    profit_125_contracts_july14
)

print(f"The profit on July 15 for the initial 25 contracts is {profit_25_contracts_initial}.\n")
print(f"The profit on July 15 for the 25 contracts bought on July 12 is {profit_25_contracts_july12}.\n")
print(f"The profit on July 15 for the 75 contracts bought on July 13 is {profit_75_contracts_july13}.\n")
print(f"The profit on July 15 for the 125 contracts bought on July 14 is {profit_125_contracts_july14}.\n")
print(f"The profit on July 15 for the 25 contracts bought on July 12 is {profit_july15}.\n")
print(f"The total profit is {total_profit}.\n")
