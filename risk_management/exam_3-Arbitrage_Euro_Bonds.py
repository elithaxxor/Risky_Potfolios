# Treasury bond futures quotes (converted to decimal form)
t_bond_futures_prices = {
    "December 2005": 102.0000,
    "March 2006": 101.7500,
    "June 2006": 101.6875,
    "September 2006": 101.4375,
    "December 2006": 101.1250
}

# Eurodollar futures implied interest rates (from problem 2)
eurodollar_implied_rates = {
    "December 2005": 4.50,  # Implied by 95.50
    "March 2006": 4.75,     # Implied by 95.25
    "June 2006": 5.00,      # Implied by 95.00
    "September 2006": 5.25, # Implied by 94.75
    "December 2006": 5.40   # Implied by 94.60
}

# Calculate the differences between bond futures prices and Eurodollar implied rates
# We'll focus on the closest expiration dates: March 2006, June 2006, and September 2006

# Points per contract
points_per_contract = 1000  # Each full point in Treasury or Eurodollar futures represents $1000

# Assume that we will sell Eurodollar futures and buy Treasury bond futures (as part of arbitrage)
# Calculate the potential arbitrage opportunity (simplified assumption)

# Selling Eurodollar futures for March, June, and September and buying Treasury futures
profit_march = (eurodollar_implied_rates["March 2006"] - 4.75) * points_per_contract
profit_june = (eurodollar_implied_rates["June 2006"] - 5.00) * points_per_contract
profit_september = (eurodollar_implied_rates["September 2006"] - 5.25) * points_per_contract

# Total profit for 100 contracts
total_arbitrage_profit = (profit_march + profit_june + profit_september) * 100  # 100 contracts

# Results
print(f"The potential arbitrage profit for March 2006 is ${profit_march:,.2f}.\n")
print(f"The potential arbitrage profit for June 2006 is ${profit_june:,.2f}.\n")
print(f"The potential arbitrage profit for September 2006 is ${profit_september:,.2f}.\n")
print(f"The total potential arbitrage profit is ${total_arbitrage_profit:,.2f}.\n")
