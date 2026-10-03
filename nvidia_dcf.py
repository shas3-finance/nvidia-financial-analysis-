# ==========================================
# NVIDIA FINANCIAL ANALYSIS - DCF
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# NVIDIA FINANCIAL ANALYSIS - DCF
# ============================================================

# ============================================================
# LOAD HISTORICAL DATA
# ============================================================

df = pd.read_csv("data/nvidia_financials.csv")

print("\nHistorical Financial Performance")
print(df)

<<<<<<< HEAD
# ==========================================
# HISTORICAL GROWTH & MARGINS
# ==========================================
=======
# ============================================================
# HISTORICAL RATIOS
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

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

# ============================================================
# REVENUE FORECAST
# Uses the same segment assumptions as revenue_forecast.py
# ============================================================

forecast_years = [2027, 2028, 2029, 2030, 2031]

historical_revenue = {
    "Data Center": 193700,
    "Gaming": 16000,
    "Professional Visualization": 3200,
    "Automotive": 2300
}

growth_assumptions = {

    "Data Center": [
        0.45,
        0.30,
        0.22,
        0.15,
        0.10
    ],

    "Gaming": [
        0.20,
        0.15,
        0.10,
        0.08,
        0.06
    ],

    "Professional Visualization": [
        0.25,
        0.20,
        0.15,
        0.12,
        0.10
    ],

    "Automotive": [
        0.25,
        0.25,
        0.20,
        0.15,
        0.12
    ]
}

segment_forecast = {}

for segment in historical_revenue:

    revenues = [historical_revenue[segment]]

    previous_revenue = historical_revenue[segment]

    for growth in growth_assumptions[segment]:

        revenue = previous_revenue * (1 + growth)

        revenues.append(revenue)

        previous_revenue = revenue

    segment_forecast[segment] = revenues

revenue_df = pd.DataFrame(
    segment_forecast,
    index=["FY2026", "FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]
)

revenue_df["Total Revenue"] = revenue_df.sum(axis=1)

forecast_revenue = (
    revenue_df.loc[
        ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"],
        "Total Revenue"
    ]
    .values
)

# ============================================================
# DCF ASSUMPTIONS
# ============================================================

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

<<<<<<< HEAD
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
=======
wacc = 0.1703
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

terminal_growth = 0.03

# $ millions

cash = 60600

debt = 10000

shares_outstanding = 24450

<<<<<<< HEAD
# ==========================================
# EBIT
# ==========================================
=======
# ============================================================
# EBIT
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

forecast_ebit = []

for revenue, margin in zip(
    forecast_revenue,
    operating_margin
):

    ebit = revenue * margin

    forecast_ebit.append(ebit)

# ============================================================
# NOPAT
# ============================================================

forecast_nopat = [

    ebit * (1 - tax_rate)

    for ebit in forecast_ebit

]

# ============================================================
# D&A
# ============================================================

forecast_da = [

    revenue * da_percent_revenue

    for revenue in forecast_revenue

]

# ============================================================
# CAPEX
# ============================================================

forecast_capex = [

    revenue * capex_percent_revenue

    for revenue in forecast_revenue

]

# ============================================================
# CHANGE IN NWC
# ============================================================

forecast_nwc = [

    revenue * change_nwc_percent_revenue

    for revenue in forecast_revenue

]

# ============================================================
# FREE CASH FLOW
# ============================================================

forecast_fcf = []

for nopat, da, capex, nwc in zip(
    forecast_nopat,
    forecast_da,
    forecast_capex,
    forecast_nwc
):

    fcf = nopat + da - capex - nwc

    forecast_fcf.append(fcf)

<<<<<<< HEAD
# ==========================================
# DISCOUNT FCF
# ==========================================
=======
# ============================================================
# DISCOUNT FCF
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

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

<<<<<<< HEAD
# ==========================================
# TERMINAL VALUE
# ==========================================
=======
# ============================================================
# TERMINAL VALUE
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

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

<<<<<<< HEAD
# ==========================================
# ENTERPRISE VALUE
# ==========================================
=======
# ============================================================
# ENTERPRISE VALUE
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

enterprise_value = (
    pv_fcf.sum()
    + pv_terminal_value
)

<<<<<<< HEAD
# ==========================================
# EQUITY VALUE
# ==========================================
=======
# ============================================================
# EQUITY VALUE
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

equity_value = (
    enterprise_value
    + cash
    - debt
)

<<<<<<< HEAD
# ==========================================
# IMPLIED SHARE PRICE
# ==========================================
=======
# ============================================================
# IMPLIED SHARE PRICE
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

implied_share_price = (
    equity_value
    / shares_outstanding
)

<<<<<<< HEAD
# ==========================================
# FORECAST TABLE
# ==========================================
=======
# ============================================================
# FORECAST TABLE
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

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

<<<<<<< HEAD
print(forecast.round(2))
=======
print(
    forecast.round(2)
)

# ============================================================
# DCF VALUATION
# ============================================================
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

# ==========================================
# DCF RESULTS
# ==========================================

print("\nDCF Valuation")
<<<<<<< HEAD
print("--------------------------------")
=======

print("------------------------------------------")
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)

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

<<<<<<< HEAD
print("--------------------------------")
=======
print("------------------------------------------")
>>>>>>> 4d1762f (Build integrated NVIDIA financial valuation model)
