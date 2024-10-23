# Define the initial values for the buying and selling prices
buy_price_32nds = 102 + 10 / 32  # 102-10
sell_price_32nds = 104 + 11 / 32  # 104-11

# Dollar value per point
dollar_value_per_point = 1000

# Calculate the dollar values of the futures contract at buying and selling
buy_price_dollar_value = buy_price_32nds * dollar_value_per_point
sell_price_dollar_value = sell_price_32nds * dollar_value_per_point

# Calculate the profit
profit = sell_price_dollar_value - buy_price_dollar_value

# Results
print(f"The dollar value of the futures contract at buying is {buy_price_dollar_value}.\n")
print(f"The dollar value of the futures contract at selling is {sell_price_dollar_value}.\n")
print(f"The profit from the futures contract is {profit}.\n")
