# Initial values
corporate_bond_yield = 7.3 / 100  # 7.3% yield to maturity
t_bond_yield = 6.0 / 100  # 6% yield on the Treasury bond

# Maturities of the corporate and Treasury bonds
corporate_bond_maturity = 19.5  # in years
t_bond_maturity = 20  # in years

# Impact of a 100 basis point (1%) rise in long-term interest rates
interest_rate_increase = 1 / 100  # 100 basis points

quality_differential = corporate_bond_yield - t_bond_yield
corporate_bond_price_change = -corporate_bond_maturity * interest_rate_increase
t_bond_price_change = -t_bond_maturity * interest_rate_increase

# Results
print(f"The quality differential between the corporate and Treasury bonds is {quality_differential:.2%}.\n")
print(f"The price change for the corporate bonds is {corporate_bond_price_change:.2%}.\n")
print(f"The price change for the Treasury bonds is {t_bond_price_change:.2%}.\n")
