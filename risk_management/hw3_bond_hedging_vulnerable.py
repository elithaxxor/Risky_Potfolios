# Define the initial values
vulnerable_bonds_face_value = 500_000_000  # $500 million
face = 110  # Face value of the bond

# Details about the hedge
futures_contracts_sold = 6000
t_bond_face_value_per_contract = 100_000  # Each T-Bond futures contract covers $100,000 face value

# Total value of T-Bond futures sold
vulnerable_bonds_market_value = vulnerable_bonds_face_value * face # 110% of face value
total_hedge_value = futures_contracts_sold * t_bond_face_value_per_contract

# Calculate the values
print(f"The market value of the vulnerable bonds is {vulnerable_bonds_market_value}.\n")
print(f'The total value of the hedge is {total_hedge_value}.\n')
