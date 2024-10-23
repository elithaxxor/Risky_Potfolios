# Description: This script calculates the profit in a bull market scenario.
contract_size = 0.0
selling_price =  0.0

# 3. Calculate Profit in Bull Market Scenario
buying_price_bull_market = 0
loss_per_gbp = selling_price - buying_price_bull_market
total_loss = loss_per_gbp * contract_size

print(
    f"\n [QUESTION #3]  [calculate loss in a bear market scenario]\n"
    f"[Given #2] Profit if GBP Falls to ${buying_price_bull_market}, and selling price is ${selling_price} \n\n "
    f"[ANSWER #2]\n "
    f"Loss per Unit: {loss_per_gbp}profit in a bear market: ${total_loss:,.2f}")
