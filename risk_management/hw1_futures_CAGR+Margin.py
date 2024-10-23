buy_back_price_usd_per_gbp = 1.08  # USD per GBP
sell_price_usd_per_gbp = 1.2847  # USD per GBP
contract_size_gbp = 62500  # GBP

# 3. Calculate the annual compound rate of return if the profit is made in 2 months.
initial_margin = 3600  # USD
time_period_months = 2  # Time period in months

gain_per_gbp = sell_price_usd_per_gbp - buy_back_price_usd_per_gbp
total_gain_usd = gain_per_gbp * contract_size_gbp
profit = total_gain_usd  # USD from the previous calculation

# CAGR formula: ((Final Value / Initial Value) ^ (12 / Months)) - 1
final_value = initial_margin + profit
CAGR = (final_value / initial_margin) ** (12 / time_period_months) - 1

# Display the calculated CAGR
print(f'The annual compound rate of return is {CAGR:.2%}.\n')
print(f'The final value is {final_value}.\n')
