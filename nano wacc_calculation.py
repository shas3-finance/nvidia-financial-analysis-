# NVIDIA WACC Calculation

# Assumptions
risk_free_rate = 0.0422
beta = 2.22
market_return = 0.10
pre_tax_cost_debt = 0.04
tax_rate = 0.18

# Capital structure
market_value_equity = 5_600_000  # $m
debt = 10_000  # $m

# CAPM
market_risk_premium = market_return - risk_free_rate
cost_of_equity = risk_free_rate + beta * market_risk_premium

# After-tax cost of debt
after_tax_cost_debt = pre_tax_cost_debt * (1 - tax_rate)

# Capital structure weights
equity_weight = market_value_equity / (market_value_equity + debt)
debt_weight = debt / (market_value_equity + debt)

# WACC
wacc = (
    equity_weight * cost_of_equity
    + debt_weight * after_tax_cost_debt
)

# Display results
print("\nNVIDIA WACC Calculation")
print("------------------------")
print(f"Risk-Free Rate: {risk_free_rate:.2%}")
print(f"Beta: {beta:.2f}")
print(f"Market Return: {market_return:.2%}")
print(f"Market Risk Premium: {market_risk_premium:.2%}")
print(f"Cost of Equity: {cost_of_equity:.2%}")
print(f"After-Tax Cost of Debt: {after_tax_cost_debt:.2%}")
print(f"Equity Weight: {equity_weight:.2%}")
print(f"Debt Weight: {debt_weight:.2%}")
print(f"\nWACC: {wacc:.2%}")
