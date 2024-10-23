sell_price_usd_per_gbp = 1.2847  # USD per GBP
contract_size_gbp = 62500  # GBP
initial_margin = 3600  # USD
time_period_months = 2  # Time period in months

margin_call_threshold = initial_margin
price_diff_margin_call = margin_call_threshold / contract_size_gbp # Price difference per GBP that would trigger a margin call


# The pound needs to strengthen to this new price to trigger a margin call
price_margin_call = sell_price_usd_per_gbp + price_diff_margin_call

print(f"The price at which a margin call would be triggered is ${price_margin_call:.4f} per GBP.")
print(f"The price difference that would trigger a margin call is ${price_diff_margin_call:.4f} per GBP.")
print(f"The margin call threshold is ${margin_call_threshold}.")
print(f"The initial margin is ${initial_margin}.")



