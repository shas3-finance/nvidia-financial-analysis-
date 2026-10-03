# ============================================================
# NVIDIA WACC CALCULATION
# ============================================================

# -----------------------------
# Market assumptions
# -----------------------------

risk_free_rate = 0.0422

beta = 2.22

market_return = 0.10

market_risk_premium = (
    market_return - risk_free_rate
)


# -----------------------------
# Cost of Equity
# CAPM
# -----------------------------

cost_of_equity = (
    risk_free_rate
    + beta * market_risk_premium
)


# -----------------------------
# Capital structure
# -----------------------------

# Replace these with the latest
# market value of equity and debt
# used in your final model.

market_value_equity = 5_600_000
market_value_debt = 10_000


total_capital = (
    market_value_equity
    + market_value_debt
)


equity_weight = (
    market_value_equity
    / total_capital
)


debt_weight = (
    market_value_debt
    / total_capital
)


# -----------------------------
# Cost of Debt
# -----------------------------

pre_tax_cost_of_debt = 0.04

tax_rate = 0.18

after_tax_cost_of_debt = (
    pre_tax_cost_of_debt
    * (1 - tax_rate)
)


# -----------------------------
# WACC
# -----------------------------

wacc = (
    equity_weight * cost_of_equity
    +
    debt_weight * after_tax_cost_of_debt
)


# -----------------------------
# Output
# -----------------------------

print("\nNVIDIA WACC Calculation")
print("-----------------------")

print(
    f"Risk-Free Rate: "
    f"{risk_free_rate:.2%}"
)

print(
    f"Beta: "
    f"{beta:.2f}"
)

print(
    f"Market Risk Premium: "
    f"{market_risk_premium:.2%}"
)

print(
    f"Cost of Equity: "
    f"{cost_of_equity:.2%}"
)

print(
    f"Equity Weight: "
    f"{equity_weight:.2%}"
)

print(
    f"Debt Weight: "
    f"{debt_weight:.2%}"
)

print(
    f"After-Tax Cost of Debt: "
    f"{after_tax_cost_of_debt:.2%}"
)

print(
    f"\nWACC: "
    f"{wacc:.2%}"
)
