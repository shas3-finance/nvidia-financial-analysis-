# ==========================================
# NVIDIA FINANCIAL ANALYSIS - DCF
# ==========================================

import pandas as pd
import numpy as np

# ==========================================
# LOAD HISTORICAL DATA
# ==========================================

df = pd.read_csv("data/nvidia_financials.csv")

print("\nHistorical Financial Performance")
print(df)

# ==========================================
# HISTORICAL GROWTH & MARGINS
# ==========================================

df["Revenue_Growth"] = df["Revenue"].pct_change()

df["Operating_Margin"] = (
    df["Operating_Income"] / df["Revenue"]
)

df["Net_Margin"] = (
    df["Net_Income"] / df["Revenue"]
)

print("\nFinancial Ratios")

print(
    df[
        [
            "Year",
            "Revenue_Growth",
            "Operating_Margin",
            "Net_Margin"
        ]
    ].round(4)
)

# ==========================================
# FORECAST ASSUMPTIONS
# ==========================================

forecast_years = [
    2027,
    2028,
    2029,
    2030,
    2031
]

revenue_growth = [
    0.30,
    0.22,
    0.16,
    0.12,
    0.08
]

operating_margin = [
    0.60,
    0.61,
    0.62,
    0.63,
    0.63
]

tax_rate = 0.18
da_percent_revenue = 0.015
capex_percent_revenue = 0.025
change_nwc_percent_revenue = 0.01

# ==========================================
# DCF ASSUMPTIONS
# ==========================================

wacc = 0.09
terminal_growth = 0.03

# NVIDIA balance sheet / share assumptions
# Values are in $ millions except shares

cash = 60600
debt = 10000
shares_outstanding = 24450

# ==========================================
# REVENUE FORECAST
# ==========================================

last_revenue = df.iloc[-1]["Revenue"]

forecast_revenue = []

for growth in revenue_growth:

    last_revenue = last_revenue * (1 + growth)

    forecast_revenue.append(last_revenue)

# ==========================================
# EBIT
# ==========================================

forecast_ebit = []

for revenue, margin in zip(
    forecast_revenue,
    operating_margin
):

    ebit = revenue * margin

    forecast_ebit.append(ebit)

# ==========================================
# NOPAT
# ==========================================

forecast_nopat = [

    ebit * (1 - tax_rate)

    for ebit in forecast_ebit

]

# ==========================================
# D&A
# ==========================================

forecast_da = [

    revenue * da_percent_revenue

    for revenue in forecast_revenue

]

# ==========================================
# CAPEX
# ==========================================

forecast_capex = [

    revenue * capex_percent_revenue

    for revenue in forecast_revenue

]

# ==========================================
# CHANGE IN NWC
# ==========================================

forecast_nwc = [

    revenue * change_nwc_percent_revenue

    for revenue in forecast_revenue

]

# ==========================================
# FREE CASH FLOW
# ==========================================

forecast_fcf = []

for nopat, da, capex, nwc in zip(
    forecast_nopat,
    forecast_da,
    forecast_capex,
    forecast_nwc
):

    fcf = nopat + da - capex - nwc

    forecast_fcf.append(fcf)

# ==========================================
# DISCOUNT FCF
# ==========================================

discount_periods = np.arange(
    1,
    len(forecast_fcf) + 1
)

discount_factors = (
    1 / (1 + wacc) ** discount_periods
)

pv_fcf = (
    np.array(forecast_fcf)
    * discount_factors
)

# ==========================================
# TERMINAL VALUE
# ==========================================

terminal_fcf = (
    forecast_fcf[-1]
    * (1 + terminal_growth)
)

terminal_value = (
    terminal_fcf
    / (wacc - terminal_growth)
)

pv_terminal_value = (
    terminal_value
    * discount_factors[-1]
)

# ==========================================
# ENTERPRISE VALUE
# ==========================================

enterprise_value = (
    pv_fcf.sum()
    + pv_terminal_value
)

# ==========================================
# EQUITY VALUE
# ==========================================

equity_value = (
    enterprise_value
    + cash
    - debt
)

# ==========================================
# IMPLIED SHARE PRICE
# ==========================================

implied_share_price = (
    equity_value
    / shares_outstanding
)

# ==========================================
# FORECAST TABLE
# ==========================================

forecast = pd.DataFrame({

    "Year": forecast_years,

    "Revenue": forecast_revenue,

    "EBIT": forecast_ebit,

    "NOPAT": forecast_nopat,

    "D&A": forecast_da,

    "Capex": forecast_capex,

    "Change_NWC": forecast_nwc,

    "FCF": forecast_fcf,

    "PV_FCF": pv_fcf

})

print("\nForecast")

print(forecast.round(2))

# ==========================================
# DCF RESULTS
# ==========================================

print("\nDCF Valuation")
print("--------------------------------")

print(
    f"WACC: {wacc:.2%}"
)

print(
    f"Terminal Growth Rate: "
    f"{terminal_growth:.2%}"
)

print(
    f"PV of Forecast FCF: "
    f"${pv_fcf.sum():,.0f} million"
)

print(
    f"Terminal Value: "
    f"${terminal_value:,.0f} million"
)

print(
    f"PV of Terminal Value: "
    f"${pv_terminal_value:,.0f} million"
)

print(
    f"Enterprise Value: "
    f"${enterprise_value:,.0f} million"
)

print(
    f"Cash: "
    f"${cash:,.0f} million"
)

print(
    f"Debt: "
    f"${debt:,.0f} million"
)

print(
    f"Equity Value: "
    f"${equity_value:,.0f} million"
)

print(
    f"Shares Outstanding: "
    f"{shares_outstanding:,.0f} million"
)

print(
    f"\nImplied Share Price: "
    f"${implied_share_price:,.2f}"
)

print("--------------------------------")
