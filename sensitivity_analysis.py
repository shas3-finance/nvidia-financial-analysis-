"""
NVIDIA Financial Analysis
DCF Sensitivity Analysis

This script calculates implied equity value per share
under different WACC and terminal growth assumptions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# MODEL INPUTS
# ============================================================

# Forecast free cash flow ($ millions)
# Replace these with the FCF figures produced by your DCF model.
forecast_fcf = {
    2027: 105000,
    2028: 130000,
    2029: 155000,
    2030: 175000,
    2031: 190000
}

# Base assumptions
base_wacc = 0.08
base_terminal_growth = 0.03

# NVIDIA balance sheet assumptions ($ millions)
cash = 60600
debt = 10000

# Diluted shares outstanding (millions)
shares_outstanding = 24500


# ============================================================
# DCF FUNCTION
# ============================================================

def calculate_dcf_value(
    fcf,
    wacc,
    terminal_growth,
    cash,
    debt,
    shares
):
    """
    Calculate enterprise value, equity value
    and implied value per share.
    """

    years = list(fcf.keys())
    fcf_values = list(fcf.values())

    # Discount forecast FCF
    pv_fcf = 0

    for i, cash_flow in enumerate(fcf_values, start=1):
        pv_fcf += cash_flow / ((1 + wacc) ** i)

    # Terminal value
    terminal_fcf = fcf_values[-1] * (1 + terminal_growth)

    terminal_value = (
        terminal_fcf /
        (wacc - terminal_growth)
    )

    # Present value of terminal value
    pv_terminal_value = (
        terminal_value /
        ((1 + wacc) ** len(fcf_values))
    )

    # Enterprise value
    enterprise_value = pv_fcf + pv_terminal_value

    # Equity value
    equity_value = enterprise_value + cash - debt

    # Implied share price
    implied_share_price = equity_value / shares

    return {
        "PV of FCF": pv_fcf,
        "PV of Terminal Value": pv_terminal_value,
        "Enterprise Value": enterprise_value,
        "Equity Value": equity_value,
        "Implied Share Price": implied_share_price
    }


# ============================================================
# SENSITIVITY TABLE
# ============================================================

wacc_values = np.arange(0.07, 0.1001, 0.005)

terminal_growth_values = np.arange(
    0.02,
    0.045,
    0.005
)

sensitivity_table = pd.DataFrame(
    index=[
        f"{wacc:.1%}"
        for wacc in wacc_values
    ],
    columns=[
        f"{growth:.1%}"
        for growth in terminal_growth_values
    ]
)


for wacc in wacc_values:

    for growth in terminal_growth_values:

        # Terminal growth must be below WACC
        if growth >= wacc:
            value = np.nan

        else:

            result = calculate_dcf_value(
                forecast_fcf,
                wacc,
                growth,
                cash,
                debt,
                shares_outstanding
            )

            value = result["Implied Share Price"]

        sensitivity_table.loc[
            f"{wacc:.1%}",
            f"{growth:.1%}"
        ] = value


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\nNVIDIA DCF SENSITIVITY ANALYSIS")
print("=" * 60)

print("\nImplied Value Per Share ($):\n")

print(
    sensitivity_table.astype(float).round(2)
)


# ============================================================
# SAVE RESULTS
# ============================================================

sensitivity_table.to_csv(
    "charts/dcf_sensitivity_table.csv"
)

print("\nSensitivity table saved to:")
print("charts/dcf_sensitivity_table.csv")


# ============================================================
# CREATE HEATMAP
# ============================================================

fig, ax = plt.subplots(figsize=(10, 7))

data = sensitivity_table.astype(float).values

im = ax.imshow(
    data,
    aspect="auto"
)

ax.set_xticks(
    range(len(terminal_growth_values))
)

ax.set_xticklabels(
    [f"{x:.1%}" for x in terminal_growth_values]
)

ax.set_yticks(
    range(len(wacc_values))
)

ax.set_yticklabels(
    [f"{x:.1%}" for x in wacc_values]
)

ax.set_xlabel("Terminal Growth Rate")
ax.set_ylabel("WACC")

ax.set_title(
    "NVIDIA DCF Sensitivity Analysis"
)

# Add values to cells
for i in range(data.shape[0]):

    for j in range(data.shape[1]):

        if not np.isnan(data[i, j]):

            ax.text(
                j,
                i,
                f"${data[i, j]:,.0f}",
                ha="center",
                va="center"
            )

fig.colorbar(
    im,
    ax=ax,
    label="Implied Value Per Share ($)"
)

plt.tight_layout()

plt.savefig(
    "charts/dcf_sensitivity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
