# Define initial values for corporate and treasury bonds
initial_corporate_yield = 7.3 / 100  # 7.3%
initial_t_bond_yield = 6.0 / 100  # 6%
corporate_yield_increase = 2.0 / 100  # 200 basis points
t_bond_yield_decrease = 1.25 / 100  # 125 basis points
# Duration (approximation) for corporate and treasury bonds
corporate_bond_duration = 19.5  # years
t_bond_duration = 20  # years
initial_vulnerable_bonds_value = 550_000_000  # $550 million market value
initial_hedge_value = 600_000_000  # $600 million

# Calculate new yields
new_corporate_yield = initial_corporate_yield + corporate_yield_increase
new_t_bond_yield = initial_t_bond_yield - t_bond_yield_decrease

# Calculate new quality differential
new_quality_differential = new_corporate_yield - new_t_bond_yield

# Calculate price change for corporate bonds
corporate_bond_price_change = -corporate_bond_duration * corporate_yield_increase

# Calculate price change for Treasury bonds
t_bond_price_change = -t_bond_duration * (-t_bond_yield_decrease)

# Loss on corporate bonds
loss_on_corporate_bonds = initial_vulnerable_bonds_value * abs(corporate_bond_price_change)

# Loss on the hedge (T-Bond futures)
loss_on_hedge = initial_hedge_value * abs(t_bond_price_change)

# Results
print(f"The new quality differential between the corporate and Treasury bonds is {new_quality_differential:.2%}.\n")
print(f"The new yield for the corporate bonds is {new_corporate_yield:.2%}.\n")
print(f"The new yield for the Treasury bonds is {new_t_bond_yield:.2%}.\n")
print(f"The price change for the corporate bonds is {corporate_bond_price_change:.2%}.\n")
print(f"The price change for the Treasury bonds is {t_bond_price_change:.2%}.\n")
print(f"The loss on the corporate bonds is {loss_on_corporate_bonds}.\n")
print(f"The loss on the hedge (T-Bond futures) is {loss_on_hedge}.\n")
