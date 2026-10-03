import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# NVIDIA REVENUE FORECAST
# Historical FY2026 + Forecast FY2027-FY2031
# $ millions
# ============================================================

years = [
    "FY2026",
    "FY2027",
    "FY2028",
    "FY2029",
    "FY2030",
    "FY2031"
]


# ------------------------------------------------------------
# FY2026 historical revenue
# ------------------------------------------------------------

historical_revenue = {
    "Data Center": 193700,
    "Gaming": 16000,
    "Professional Visualization": 3200,
    "Automotive": 2300
}


# ------------------------------------------------------------
# Forecast growth assumptions
# These are MODEL ASSUMPTIONS, not NVIDIA guidance.
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Build forecast
# ------------------------------------------------------------

forecast = {
    "Data Center": [historical_revenue["Data Center"]],
    "Gaming": [historical_revenue["Gaming"]],
    "Professional Visualization": [
        historical_revenue["Professional Visualization"]
    ],
    "Automotive": [historical_revenue["Automotive"]]
}


for segment in forecast:

    previous_revenue = forecast[segment][0]

    for growth in growth_assumptions[segment]:

        revenue = previous_revenue * (1 + growth)

        forecast[segment].append(revenue)

        previous_revenue = revenue


# ------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------

df = pd.DataFrame(
    forecast,
    index=years
)


df["Total Revenue"] = df.sum(axis=1)


# ------------------------------------------------------------
# Calculate segment mix
# ------------------------------------------------------------

for segment in forecast:

    df[f"{segment} % of Revenue"] = (
        df[segment] / df["Total Revenue"]
    )


# ------------------------------------------------------------
# Display forecast
# ------------------------------------------------------------

print("\nNVIDIA Revenue Forecast")
print(
    df[
        [
            "Data Center",
            "Gaming",
            "Professional Visualization",
            "Automotive",
            "Total Revenue"
        ]
    ].round(0)
)


# ------------------------------------------------------------
# Calculate total revenue growth
# ------------------------------------------------------------

df["Revenue Growth"] = (
    df["Total Revenue"].pct_change()
)


print("\nTotal Revenue Growth")
print(
    df["Revenue Growth"].round(4)
)


# ------------------------------------------------------------
# Calculate CAGR
# ------------------------------------------------------------

initial_revenue = df.loc["FY2026", "Total Revenue"]
final_revenue = df.loc["FY2031", "Total Revenue"]

cagr = (
    (final_revenue / initial_revenue)
    ** (1 / 5)
    - 1
)

print(
    f"\nFY2026-FY2031 Revenue CAGR: "
    f"{cagr:.2%}"
)


# ------------------------------------------------------------
# Revenue chart
# ------------------------------------------------------------

df[
    [
        "Data Center",
        "Gaming",
        "Professional Visualization",
        "Automotive"
    ]
].plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("NVIDIA Revenue Forecast by Market Platform")
plt.ylabel("Revenue ($ millions)")
plt.xlabel("Fiscal Year")
plt.tight_layout()

plt.show()
