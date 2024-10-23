# Initial values for Eurodollar futures
sell_price_eurodollar = 97.38  # Sold at this price
new_eurodollar_rate = 3.12  # New implied short-term rate

# Calculate the new Eurodollar futures price
new_price_eurodollar = 100 - new_eurodollar_rate

# Calculate the price change
price_change_eurodollar = sell_price_eurodollar - new_price_eurodollar

# Calculate profit per contract
profit_per_contract_eurodollar = price_change_eurodollar * 100 * 25  # Each point is worth $25

# Total profit for 10 contracts
total_profit_eurodollar = profit_per_contract_eurodollar * 10

# Results
print(f"The new price of the Eurodollar futures contract is {new_price_eurodollar}.\n")
print(f"The profit per contract is {profit_per_contract_eurodollar}.\n")
print(f"The total profit for 10 contracts is {total_profit_eurodollar}.\n")
print(f"The new Eurodollar rate is {new_eurodollar_rate}.\n")
print(f"The price change is {price_change_eurodollar}.\n")
