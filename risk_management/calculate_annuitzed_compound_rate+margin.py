# 4. Calculate Annualized Compound Rate of Return
print(
    "\n3. [Question #3] Calculating Annualized Compound Rate of Return, when given [Margin] and [Investment Horizon]...\n")

# 1. User Inputs
contract_size = 0.0
selling_price =  0.0
buying_price_bear_market = 0.0

# 2. Calculate Profit in Bear Market Scenario
total_value = contract_size * selling_price
profit_per_gbp = selling_price - buying_price_bear_market
total_profit_bear = profit_per_gbp * contract_size

initial_margin = 0.0
investment_horizon = 0.0
r = total_profit_bear / initial_margin
annualized_return = (((1 + total_profit_bear) / initial_margin) ** (12 / investment_horizon)) - 1

print(f"\n [ANSWER #3]\n r = {r}\n annualized_return = {annualized_return}")
