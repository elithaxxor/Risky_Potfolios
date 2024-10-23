 #Define the initial values for the Eurodollar futures contract
sell_price_eurodollar = 98.70
buy_price_eurodollar = 98.90

# Calculate the price change
price_change_eurodollar = buy_price_eurodollar - sell_price_eurodollar

# Dollar loss calculation: each 0.01 change equals $25 on a $1 million contract
loss_per_basis_point = 25
loss = price_change_eurodollar * 100 * loss_per_basis_point

# Result

print(f"The price change for the Eurodollar futures contract is {price_change_eurodollar}.\n")
print(f"The loss per basis point is {loss_per_basis_point}.\n")
print(f"The total loss for the contract is {loss}.\n")

