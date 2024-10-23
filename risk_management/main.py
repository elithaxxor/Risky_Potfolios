def calculate_quality_differntial(vuln_fund_yield, t_bond_coupon_yield):
    print("Calculating the quality differential.")

    quality_differential = vuln_fund_yield - t_bond_coupon_yield  # Quality Differential
    print(f"Quality Differential: {quality_differential}")

    return quality_differential

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

def calculate_hedge_effectiveness():
    print(" [Question #2]- Evaluate hedge effectiveness under specified conditions \n [long-term rate of interest rises] ")

    delta_yield = float(input("Enter the change in long term interest yield: [In BP] eg: 100 bp"))
    delta_yield_percent = delta_yield / 100
    notional_per_contract = 100000  # $100,000 per contract
    contract_size = float(input("Enter the contract size of the bond: "))
    face = 100 # Face value of the bond


    # Corp Bond corp bond price
    print("Enter the following details for the [corporate bond]: \n")
    corporate_bond_yield = float(input("[c-bond] Enter the yield of the corporate bond: "))
    corp_bond_duration = float(input("[c-bond] Enter the duration of the corporate bond: "))
    percent_over_par = float(input("[c-bond] Enter the percent over par of the corporate bond: "))
    total_corp_bond_value = float(input("[c-bond]  Enter the total value of the corporate bond: [Total Value in USD]"))
    corp_bond_face_value = total_corp_bond_value / (1 + percent_over_par)

    # T-Bond Info bond price
    print("\nEnter the following details for the [t-bond]: \n")
    t_bond_coupon_yield = float(input("[t-bond]  Enter the coupon yield of the T-bond: "))
    t_bond_ytm_INITIAL = float(input("[t-bond]  Enter the yield to maturity of the T-bond: "))
    t_bond_duration = float(input("[t-bond]  Enter the duration of the T-bond: "))
    t_bond_face_value = 100  # Face value of the bond

    t_bond_coupon_rate = t_bond_coupon_yield / 100  # as decimal
    t_bond_ytm_NEW = t_bond_ytm_INITIAL + delta_yield_percent # New yield to maturity
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




#############################
def calculate_total_value(contract_size, selling_price):
    return contract_size * selling_price

def calculate_profit(selling_price, buying_price, contract_size):
    profit_per_gbp = selling_price - buying_price
    total_profit = profit_per_gbp * contract_size
    return total_profit

def calculate_loss(selling_price, buying_price, contract_size):
    loss_per_gbp = selling_price - buying_price
    total_loss = loss_per_gbp * contract_size
    return total_loss

def calculate_annualized_return(profit, margin, months):

    r = profit / margin
    periods = 12 / months
    annualized_return = (((1 + profit) / margin) ** (12 / months)) - 1

    print("r", r)
    print("periods", periods)
    print("annualized_return", annualized_return)
    return annualized_return * 100  # Convert to percentage

#################################################

def Futures_Contract_Calculator():

    def display_menu():
        """
        Display the menu options to the user.
        """
        print("=== British Pound (GBP) Futures Contract Calculator ===\n")

        # 1. User Inputs
        print("Please enter the following details for your GBP futures contract:\n")

        # Question 1
        print(" [Question #1] Calculating Total Value of the Futures Contract...\n")
        contract_size = float(input(" Contract Original Size (Number of GBP): "))
        selling_price = float(input(" Selling Original Price (USD per GBP): "))
        total_value = calculate_total_value(contract_size, selling_price)

        print("\n\n[MENU] \n Select the question you want to solve:")
        print("2. Calculate Profit in Bear Market Scenario")
        print("3. Calculate Annualized Compound Rate of Return")
        print("4. Calculate Loss in Bull Market Scenario")
        print("5. Exit")
        global profit_bear
        profit_bear = 0

        while True:
           # display_menu()
            print(f"\n\n[ANSWER #1] Total Value of the Futures Contract: \n${total_value:,.2f}\n\n")
            choice = input("\nEnter the number corresponding to your choice (2-4): ")

            if choice == '2':
                profit_bear = question_2(selling_price, contract_size)
            elif choice == '3':
                question_3(profit_bear)
            elif choice == '4':
                question_4(selling_price, contract_size)
            elif choice == '5':
                print(". Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option (1-5).\n")

    # Question 2
    def question_2(selling_price, contract_size):
        print("\n2. [Question #2] Calculating Profit in Bear Market Scenario...\n")
        buying_price_bear = float(input("\nEnter Buying Price in Bear Market Scenario [price GPB Falls too](USD per GBP): "))
        profit_bear = calculate_profit(selling_price, buying_price_bear, contract_size)
        print(f"\n [GIVEN #2] Profit if GBP Falls to ${buying_price_bear}, and selling price is ${selling_price} \n\n [ANSWER #2]profit in a bear market: ${profit_bear:,.2f}")
        return profit_bear
    # Question 3
    def question_3(profit_bear):
        print("\n3. [Question #3] Calculating Annualized Compound Rate of Return, when given [Margin] and [Investment Horizon]...\n")
        initial_margin = float(input("Enter Initial Margin Deposit (USD): "))
        investment_horizon = float(input("\nWhen do you expect to make a profit? "
                                         "\n EnterInvestment Horizon (Months): \n"))
        annuatized_return = calculate_annualized_return(profit_bear, initial_margin, investment_horizon)
        print(f" \n[GIVEN #3] Annualized Compound Rate of Return, when \n* profit/loss = {profit_bear}, time horizon = {investment_horizon}, and initial_margin = {initial_margin}: \n\n [ANSWER #3] [Annutized Return] = {annuatized_return:.2f}%")

    # Question 4
    def question_4(selling_price, contract_size):
        print("\n4. [Question #4] Calculating Loss in Bull Market Scenario...\n")
        buying_price_bull = float(input(" Buying Price in Bull Market Scenario [Market Recovery] (USD per GBP): "))
        loss_bull = calculate_loss(selling_price, buying_price_bull, contract_size)
        print(f" [GIVEN #4] Loss if GBP Rises to : ${buying_price_bull}: and is sold at: $ {selling_price} \n [ANSWER #4].[Profit/Loss] = {loss_bull:,.2f}")


    display_menu()
##################################################

def Bond_Pricing_Calculator():


    print("Enter the following details for the bond: \n")



    print("Bond Pricing Calculator!")

    def display_menu():
        print("\n\n[MENU] \n Select the question you want to solve:")
        print("1. [Question A]  Calculates the quality differential.")
        print("2. [Question B] Evaluates hedge effectiveness under specified conditions.")

        while True:
            # display_menu()
            choice = input("\nEnter the number corresponding to your choice (2-4): ")

            if choice == '1':
                print("\n[Question A]  Calculates the quality differential.\n")
                # Question 1- Calculate the quality differential
                vuln_fund_yield = float(input("Enter the yield of the (risky) vulnerable bond: "))
                t_bond_coupon_yield = float(input("Enter the yield of the (non-risk) T-bond coupon: "))
                quality_differential = calculate_quality_differntial(vuln_fund_yield, t_bond_coupon_yield)

                print("\n[Answer A] Quality Differential: ", quality_differential)

            if choice == '2':
                print("\n[Question B] Evaluates hedge effectiveness under specified conditions.\n")
                calculate_hedge_effectiveness()
               # print("\n[Answer B] Hedge Effectiveness: ", hedge_effectiveness)

            elif choice == '3':
                print("\nThank you for using the GBP Futures Contract Calculator. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option (1-5).\n")

    display_menu()



def main():

    print("Enter Choices corresponding to the homeworks you want to solve: ")
    print("1. [HW 1] Futures Contract Calculator")
    print("2. [HW 2] Bond Pricing Calculator")

    choice = input("Enter your choice: ")
    if choice == '1':
        print("(GBP) [HW 1] Futures Contract Calculator!")
        Futures_Contract_Calculator()
    if choice == '2':
        print("Bond Pricing Calculator!")
        Bond_Pricing_Calculator()


if __name__ == "__main__":
    main()