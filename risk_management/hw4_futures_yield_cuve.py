# Initial values
buy_price_t_bond = 103 + 31 / 32  # 103-31 in decimal form
basis_point_change = 50  # Basis point decrease in yield (0.50%)
contracts = 10  # Number of contracts
dollar_increase_per_basis_point = 1  # Rough estimate: 1 point per basis point

# Calculate the price increase for the treasury bond
price_increase = basis_point_change * dollar_increase_per_basis_point

# Calculate the new price of the treasury bond futures contract
new_price_t_bond = buy_price_t_bond + price_increase

# Profit per contract (new price - buy price)
profit_per_contract = price_increase

# Total profit for 10 contracts
total_profit = profit_per_contract * contracts * 1000  # Each point is worth $1000

# Results

print(f"The price increase for the T-Bond futures contract is {price_increase}.\n")
print(f"The new price of the T-Bond futures contract is {new_price_t_bond}.\n")
print(f"The profit per contract is {profit_per_contract * 1000}.\n")
print(f"The total profit for 10 contracts is {total_profit}.\n")