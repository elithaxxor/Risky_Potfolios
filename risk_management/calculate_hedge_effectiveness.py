print(" [Question #2]- Evaluate hedge effectiveness under specified conditions \n [long-term rate of interest rises] ")


def calculate_macaulay_duration(face_value, coupon_rate, ytm, years):
    """
    Calculate the Macaulay Duration of a bond.

    Parameters:
    face_value (float): Face value of the bond ($)
    coupon_rate (float): Annual coupon rate of the bond (%)
    ytm (float): Yield to maturity of the bond (%)
    years (int): Number of years until maturity

    Returns:
    float: Macaulay Duration (years)
    """
    cash_flow = coupon_rate * face_value

    print("cash_flow: ", cash_flow)
    print("pv_face_value: ", face_value / (1 + ytm)**years)

    pv_fv = face_value / (1 + ytm)**years
    pv_coupons = [int(cash_flow) / (1 + int(ytm)) ** t for t in range(1, int(years) + 1)]
    price = sum(pv_coupons) + pv_fv
    print("PV Face Value: ", pv_fv)
    print("Price: ", price)
    print("PV Coupons: ", pv_coupons)

    weighted_cash_flow = sum(t * pv_coupons[t-1] for t in range(1, int(years) + 1)) + int(years) * int(pv_fv)
    macaulay_duration = weighted_cash_flow / price

    print("Weighted Cash Flow: ", weighted_cash_flow)
    print("Macaulay Duration: ", macaulay_duration)

    return macaulay_duration

def calculate_modified_duration(macaulay_duration, ytm):
    """
    Calculate the Modified Duration of a bond.

    Parameters:
    macaulay_duration (float): Macaulay Duration (years)
    ytm (float): Yield to maturity of the bond (%)

    Returns:
    float: Modified Duration (years)
    """
    return macaulay_duration / (1 + ytm)

print("[delta yield] Enter the change in long term interest yield: [In BP] eg: 100 bp")
delta_yield = 0.0
delta_yield_percent = delta_yield / 100
notional_per_contract = 100000  # $100,000 per contract
contract_size = 0.0
face = 100  # Face value of the bond

# Corp Bond corp bond price
print("Enter the following details for the [corporate bond]: \n")
corporate_bond_yield = 0.0
corp_bond_duration = 0.0
percent_over_par = 0.0
total_corp_bond_value = 0.0
corp_bond_face_value = total_corp_bond_value / (1 + percent_over_par)

# T-Bond Info bond price
print("\nEnter the following details for the [t-bond]: \n")
t_bond_coupon_yield = 0.0
t_bond_ytm_INITIAL = 0.0
t_bond_duration = 0.0
t_bond_face_value = 100  # Face value of the bond

t_bond_coupon_rate = t_bond_coupon_yield / 100  # as decimal
t_bond_ytm_NEW = t_bond_ytm_INITIAL + delta_yield_percent  # New yield to maturity
ytm_initial = t_bond_ytm_INITIAL / 100  # as decimal

# Calculate the new price of the T-bond


# Price Change = -Duration * Delta Yield
price_change_corp = -corp_bond_duration * (delta_yield / 100)  # as a decimal
loss_corp = price_change_corp * total_corp_bond_value  # $500 million

macaulay_duration_t = calculate_macaulay_duration(t_bond_face_value, t_bond_coupon_rate, ytm_initial, t_bond_duration)
modified_duration_t = calculate_modified_duration(macaulay_duration_t, ytm_initial)

print("delta yield percent: ", delta_yield_percent)
print("Corporate Bond Face Value:   ", corp_bond_face_value)
print("delta yield,", delta_yield)
print("delta yield percent: ", delta_yield_percent)
print("new t_bond YTM: ", t_bond_ytm_NEW)

print("\n [ANSWER #2] Hedge Effectiveness: \n")
print("Macaulay Duration T-Bond: ", macaulay_duration_t)
print("Price Change Corp: ", price_change_corp)
print("Loss Corp: ", loss_corp)

# Calculate Gain on Futures Contracts
# When rates rise, futures prices fall, and since you sold futures, you gain
# Gain per contract = Modified Duration * Delta Yield * Notional
gain_per_contract = modified_duration_t * (delta_yield / 100) * notional_per_contract
total_gain_futures = gain_per_contract * contract_size

# Net Effect
net_effect = loss_corp + total_gain_futures  # loss_corp is negative

print(f"Initial Yield of Corporate Bonds: {corporate_bond_yield:.2f}%")
print(f"Initial Yield of Treasury Bond: {t_bond_ytm_INITIAL:.2f}%")
print(f"Delta Yield (Rate Increase): {delta_yield:.2f}%\n")

print(f"\n[ANSWER]\n Face Value of Vulnerable Corporate Bonds: ${corp_bond_face_value:,.2f}")
print(f"Price Change on Corporate Bonds: {price_change_corp * 100:.2f}%")
print(f"Loss on Corporate Bonds: ${loss_corp:,.2f}\n")

print(f"\n [ANSWER\ \n Macaulay Duration of 20-Year 6% T-Bond: {macaulay_duration_t:.2f} years")
print(f"Modified Duration of T-Bond: {modified_duration_t:.2f} years")

print(f"\n[Answer] \n Gain per Futures Contract: ${gain_per_contract:,.2f}")
print(f"Total Gain on {contract_size} Futures Contracts: ${total_gain_futures:,.2f}\n")

print(f"\n[Answer] \n Net Effect of Hedge: ${net_effect:,.2f}")
if net_effect < 0:
    print("Overall, the hedge reduces the loss but does not fully offset it.\n")
elif net_effect > 0:
    print("Overall, the hedge results in a net gain.\n")
else:
    print("Overall, the hedge perfectly offsets the loss.\n")



