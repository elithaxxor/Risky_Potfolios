contract_size_gbp = 62500  # GBP
sell_price_usd_per_gbp = 1.2847  # USD per GBP

# Total value of the British pounds in USD
total_value_usd = contract_size_gbp * sell_price_usd_per_gbp

# Result
print(f"The total value in USD of the British pounds covered by the futures contract is ${total_value_usd:,.2f}.\n")
