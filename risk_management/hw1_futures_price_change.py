# 2. Calculate the dollar amount of gain if the British pound falls to $1.08.
buy_back_price_usd_per_gbp = 1.08  # USD per GBP
sell_price_usd_per_gbp = 1.2847  # USD per GBP
contract_size_gbp = 62500  # GBP

# Gain per GBP
gain_per_gbp = sell_price_usd_per_gbp - buy_back_price_usd_per_gbp
# Total gain in USD
total_gain_usd = gain_per_gbp * contract_size_gbp

# Result
print(f"The gain per GBP is {gain_per_gbp}.\n")
print(f"The total gain in USD is {total_gain_usd}.\n")


