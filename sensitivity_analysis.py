import numpy as np
import matplotlib.pyplot as plt

from assumptions import (
    WACC,
    TERMINAL_GROWTH_RATE,
    CASH,
    DEBT,
    SHARES_OUTSTANDING
)


# --------------------------------------------------
# NVIDIA DCF Sensitivity Analysis
# --------------------------------------------------

# Forecast Free Cash Flow ($ millions)
forecast_fcf = np.array([
    144875.68,
    189966.28,
    234223.16,
    272952.46,
    299775.91
])


# Sensitivity ranges
wacc_values = [
    0.15,
    0.16,
    WACC,
    0.18,
    0.19
]

terminal_growth_values = [
    0.02,
    0.025,
    TERMINAL_GROWTH_RATE,
    0.035,
    0.04
]


def calculate_share_price(wacc, terminal_growth):

    # Present value of forecast FCF
    pv_fcf = 0

    for year, fcf in enumerate(forecast_fcf, start=1):

        pv_fcf += (
            fcf / ((1 + wacc) ** year)
        )

    # Terminal value
    terminal_fcf = (
        forecast_fcf[-1]
        * (1 + terminal_growth)
    )

    terminal_value = (
        terminal_fcf
        / (wacc - terminal_growth)
    )

    # Present value of terminal value
    pv_terminal_value = (
        terminal_value
        / ((1 + wacc) ** 5)
    )

    # Enterprise value
    enterprise_value = (
        pv_fcf
        + pv_terminal_value
    )

    # Equity value
    equity_value = (
        enterprise_value
        + CASH
        - DEBT
    )

    # Implied share price
    share_price = (
        equity_value
        / SHARES_OUTSTANDING
    )

    return share_price


# --------------------------------------------------
# Print Sensitivity Table
# --------------------------------------------------

print("\nNVIDIA DCF Sensitivity Analysis")
print("=" * 75)

print("\nImplied Share Price ($)")
print("Terminal Growth →")

header = "WACC       "

for growth in terminal_growth_values:
    header += f"{growth:.2%}       "

print(header)
print("-" * 75)


for wacc in wacc_values:

    row = f"{wacc:.2%}     "

    for growth in terminal_growth_values:

        price = calculate_share_price(
            wacc,
            growth
        )

        row += f"${price:,.2f}     "

    print(row)


# --------------------------------------------------
# Central Case
# --------------------------------------------------

central_price = calculate_share_price(
    WACC,
    TERMINAL_GROWTH_RATE
)

print("\nCentral Case")
print("-" * 35)

print(f"WACC: {WACC:.2%}")
print(
    f"Terminal Growth: "
    f"{TERMINAL_GROWTH_RATE:.2%}"
)

print(
    f"Implied Share Price: "
    f"${central_price:,.2f}"
)
# --------------------------------------------------
# Sensitivity Heatmap
# --------------------------------------------------

sensitivity_matrix = np.zeros(
    (
        len(terminal_growth_values),
        len(wacc_values)
    )
)

for i, growth in enumerate(terminal_growth_values):

    for j, wacc in enumerate(wacc_values):

        sensitivity_matrix[i, j] = calculate_share_price(
            wacc,
            growth
        )


plt.figure(figsize=(10, 6))

plt.imshow(
    sensitivity_matrix,
    aspect="auto"
)

plt.colorbar(
    label="Implied Share Price ($)"
)

plt.xticks(
    range(len(wacc_values)),
    [f"{w:.2%}" for w in wacc_values]
)

plt.yticks(
    range(len(terminal_growth_values)),
    [f"{g:.2%}" for g in terminal_growth_values]
)

plt.xlabel("WACC")
plt.ylabel("Terminal Growth Rate")

plt.title(
    "NVIDIA DCF Sensitivity Analysis"
)

plt.tight_layout()

plt.savefig(
    "sensitivity_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(
    "\nSensitivity chart saved as "
    "sensitivity_analysis.png"
)
