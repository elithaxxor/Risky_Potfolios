# Given values
loan_amount = 200_000_000  # $200 million
bank_min_profit = 0.005  # 0.5% profit margin
cash_market_rate = 4.5 / 100  # 4.5% Eurodollar CD yield in cash market

# Implied interest rates from Eurodollar futures (converted from futures quotes)
implied_rate_dec_2005 = 100 - 95.50  # 4.50%
implied_rate_mar_2006 = 100 - 95.25  # 4.75%
implied_rate_jun_2006 = 100 - 95.00  # 5.00%
implied_rate_sep_2006 = 100 - 94.75  # 5.25%

# Calculate the average implied interest rate for the year
average_implied_rate = (implied_rate_dec_2005 + implied_rate_mar_2006 + implied_rate_jun_2006 + implied_rate_sep_2006) / 4

# Add the bank's minimum profit margin
lowest_annual_rate = average_implied_rate + (bank_min_profit * 100)  # in percentage terms

# Result: the lowest fixed annual rate the bank can charge
print(f"The lowest fixed annual rate the bank can charge is {lowest_annual_rate:.2f}%.")
print(f"the average implied interest rate for the year is {average_implied_rate:.2f}%")
