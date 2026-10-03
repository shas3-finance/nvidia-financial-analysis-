# NVIDIA Financial Analysis

A Python-based financial modelling project analysing NVIDIA's historical financial performance, revenue growth, WACC, discounted cash flow (DCF) valuation, and valuation sensitivity.

## Overview

This project develops an integrated financial model for NVIDIA Corporation using Python.

The model covers:

* Historical financial analysis
* Segment-based revenue forecasting
* Weighted Average Cost of Capital (WACC)
* Free Cash Flow (FCF) forecasting
* Discounted Cash Flow (DCF) valuation
* WACC and terminal growth sensitivity analysis
* Financial modelling visualisations

The project is designed to demonstrate practical financial modelling, valuation, data analysis and Python programming skills relevant to investment banking, asset management, equity research and private credit.

## Project Structure

```text
nvidia-financial-analysis/
│
├── data/
│   └── nvidia_financials.csv
│
├── assumptions.py
├── revenue_forecast.py
├── wacc_calculation.py
├── nvidia_dcf.py
├── sensitivity_analysis.py
│
├── revenue_forecast.png
├── sensitivity_analysis.png
│
├── .gitignore
└── README.md
```

## Model Workflow

```text
Historical Financial Data
          │
          ▼
Revenue Forecast
          │
          ▼
Operating Forecast
          │
          ▼
Free Cash Flow
          │
          ▼
WACC
          │
          ▼
DCF Valuation
          │
          ▼
Sensitivity Analysis
```

## Revenue Forecast

Revenue is forecast by business segment using individual growth assumptions for:

* Data Center
* Gaming
* Professional Visualization
* Automotive

The model calculates:

* Segment revenue
* Total revenue
* Revenue growth
* Revenue mix
* FY2026–FY2031 revenue CAGR

The current base-case model produces approximately **22.9% revenue CAGR from FY2026 to FY2031**.

## WACC Calculation

The WACC model uses the Capital Asset Pricing Model (CAPM) to estimate the cost of equity.

Key inputs include:

* Risk-free rate
* Beta
* Expected market return
* Market value of equity
* Market value of debt
* Pre-tax cost of debt
* Tax rate

The current model produces a **17.03% WACC** based on the assumptions contained in `assumptions.py`.

These assumptions are intended for modelling purposes and should be updated with current market data when the model is used for an investment decision.

## DCF Valuation

The DCF model forecasts NVIDIA's Free Cash Flow over FY2027–FY2031.

The model calculates:

1. Revenue
2. EBIT
3. Taxes
4. NOPAT
5. Depreciation & Amortisation
6. Capital Expenditure
7. Change in Net Working Capital
8. Free Cash Flow
9. Present Value of Free Cash Flow
10. Terminal Value
11. Enterprise Value
12. Equity Value
13. Implied Share Price

### Current Base-Case Valuation

| Metric              |      Value |
| ------------------- | ---------: |
| WACC                |     17.03% |
| Terminal Growth     |      3.00% |
| PV of Forecast FCF  |   $690.7bn |
| Terminal Value      |    $2.20tn |
| Enterprise Value    |    $1.69tn |
| Equity Value        |    $1.74tn |
| Implied Share Price | **$71.32** |

The valuation is highly sensitive to the WACC and terminal growth assumptions, which is why the model includes a dedicated sensitivity analysis.

## Sensitivity Analysis

The sensitivity model evaluates the implied share price across different combinations of:

* WACC
* Terminal growth rate

The current analysis tests WACC from **15% to 19%** and terminal growth from **2% to 4%**.

This allows the effect of changes in key DCF assumptions to be assessed rather than relying on a single valuation point.

## Visualisations

The project generates visual outputs including:

* Revenue forecast by segment
* DCF sensitivity analysis

These charts are saved as PNG files and can be incorporated into presentations or investment analysis.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Git
* GitHub

## Key Skills Demonstrated

### Financial Modelling

* Revenue forecasting
* Financial statement analysis
* WACC calculation
* Free Cash Flow modelling
* DCF valuation
* Terminal value calculation
* Sensitivity analysis

### Data Analysis

* Pandas
* NumPy
* Financial ratio analysis
* Data manipulation
* Data visualisation

### Programming

* Python functions
* Modular assumptions
* DataFrames
* Iterative forecasting
* Model automation
* Git version control

## Disclaimer

This project is for educational and portfolio purposes only. The assumptions and valuation outputs are illustrative and should not be interpreted as investment advice or a recommendation to buy or sell securities.

