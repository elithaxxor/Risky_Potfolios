print("\n2. [Question #2] Calculating Profit in Bear Market Scenario...\n")

# 1. User Inputs
contract_size = 0.0
selling_price =  0.0
buying_price_bear_market = 0.0

# 2. Calculate Profit in Bear Market Scenario
total_value = contract_size * selling_price
profit_per_gbp = selling_price - buying_price_bear_market
total_profit_bear = profit_per_gbp * contract_size

print(
    f"\n [QUESTION #1] [calculate the profit in a bear market scenario]\n"
    f"[GIVEN #1] Profit if GBP Falls to ${buying_price_bear_market}, and selling price is ${selling_price} and contract_size: {contract_size}\n\n\n [ANSWER #2] \n"
    f"total_value: ${total_value:,.2f}\n"
    f"total_profit: ${total_profit_bear:,.2f}\n"
    f"profit per GBP: ${profit_per_gbp:,.2f}\n"
    f"profit in a bear market: ${total_profit_bear:,.2f}")

# 3. Calculate Profit in Bull Market Scenario
buying_price_bull_market = 0
loss_per_gbp = selling_price - buying_price_bull_market
total_loss = loss_per_gbp * contract_size


print(
    f"\n [QUESTION #3]  [calculate loss in a bear market scenario]\n"
    f"[Given #2] Profit if GBP Falls to ${buying_price_bull_market}, and selling price is ${selling_price} \n\n "
    f"[ANSWER #2]\n "
    f"Loss per Unit: {loss_per_gbp}profit in a bear market: ${total_loss:,.2f}")

# 4. Calculate Annualized Compound Rate of Return
print(
    "\n3. [Question #3] Calculating Annualized Compound Rate of Return, when given [Margin] and [Investment Horizon]...\n")
initial_margin = 0.0
investment_horizon = 0.0
r = total_profit_bear / initial_margin
annualized_return = (((1 + total_profit_bear) / initial_margin) ** (12 / investment_horizon)) - 1

print(f"\n [ANSWER #3]\n r = {r}\n annualized_return = {annualized_return}")
