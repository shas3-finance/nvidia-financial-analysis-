# NVIDIA Financial Analysis
# Central Model Assumptions

# --------------------------------------------------
# Revenue Forecast
# --------------------------------------------------

HISTORICAL_REVENUE = {
    "Data Center": 193700,
    "Gaming": 16000,
    "Professional Visualization": 3200,
    "Automotive": 2300
}

GROWTH_ASSUMPTIONS = {
    "Data Center": [0.45, 0.30, 0.22, 0.15, 0.10],
    "Gaming": [0.20, 0.15, 0.10, 0.08, 0.06],
    "Professional Visualization": [0.25, 0.20, 0.15, 0.12, 0.10],
    "Automotive": [0.25, 0.25, 0.20, 0.15, 0.12]
}

# --------------------------------------------------
# Operating Assumptions
# --------------------------------------------------

OPERATING_MARGINS = [
    0.60,
    0.61,
    0.62,
    0.63,
    0.63
]

TAX_RATE = 0.18

DA_PERCENT_REVENUE = 0.015
CAPEX_PERCENT_REVENUE = 0.025
NWC_PERCENT_REVENUE = 0.01

# --------------------------------------------------
# WACC Assumptions
# --------------------------------------------------

RISK_FREE_RATE = 0.0422
BETA = 2.22
MARKET_RETURN = 0.10

MARKET_VALUE_EQUITY = 5_600_000
MARKET_VALUE_DEBT = 10_000

PRE_TAX_COST_OF_DEBT = 0.04

# --------------------------------------------------
# DCF Assumptions
# --------------------------------------------------

WACC = 0.1703
TERMINAL_GROWTH_RATE = 0.03

CASH = 60_600
DEBT = 10_000
SHARES_OUTSTANDING = 24_450
