import pandas as pd
import matplotlib.pyplot as plt

from assumptions import (
    HISTORICAL_REVENUE,
    GROWTH_ASSUMPTIONS
)


# --------------------------------------------------
# NVIDIA Revenue Forecast
# --------------------------------------------------

years = [
    "FY2026",
    "FY2027",
    "FY2028",
    "FY2029",
    "FY2030",
    "FY2031"
]


# Start forecast with historical revenue
forecast = {
    segment: [revenue]
    for segment, revenue in HISTORICAL_REVENUE.items()
}


# Apply growth assumptions
for segment in forecast:

    previous_revenue = forecast[segment][0]

    for growth in GROWTH_ASSUMPTIONS[segment]:

        revenue = previous_revenue * (1 + growth)

        forecast[segment].append(revenue)

        previous_revenue = revenue


# Create DataFrame
df = pd.DataFrame(
    forecast,
    index=years
)


# Calculate total revenue
df["Total Revenue"] = df.sum(axis=1)


# --------------------------------------------------
# Display Forecast
# --------------------------------------------------

print("\nNVIDIA Revenue Forecast")
print("=" * 80)

print(
    df[
        [
            "Data Center",
            "Gaming",
            "Professional Visualization",
            "Automotive",
            "Total Revenue"
        ]
    ].round(2)
)


# --------------------------------------------------
# Revenue Growth
# --------------------------------------------------

df["Revenue Growth"] = df["Total Revenue"].pct_change()

print("\nRevenue Growth")
print("=" * 40)

print(
    df["Revenue Growth"]
    .mul(100)
    .round(2)
    .astype(str)
    + "%"
)


# --------------------------------------------------
# Revenue CAGR
# --------------------------------------------------

initial_revenue = df.loc["FY2026", "Total Revenue"]
final_revenue = df.loc["FY2031", "Total Revenue"]

cagr = (
    (final_revenue / initial_revenue) ** (1 / 5)
) - 1

print("\nRevenue CAGR")
print("=" * 40)

print(f"FY2026-FY2031 CAGR: {cagr:.2%}")


# --------------------------------------------------
# Revenue Mix
# --------------------------------------------------

print("\nRevenue Mix")
print("=" * 80)

for segment in HISTORICAL_REVENUE:

    df[f"{segment} % of Revenue"] = (
        df[segment] / df["Total Revenue"]
    )

print(
    df[
        [
            "Data Center",
            "Gaming",
            "Professional Visualization",
            "Automotive"
        ]
    ].div(df["Total Revenue"], axis=0)
    .mul(100)
    .round(2)
    .astype(str)
    + "%"
)


# --------------------------------------------------
# Revenue Forecast Chart
# --------------------------------------------------

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

plt.title("NVIDIA Revenue Forecast by Segment")
plt.xlabel("Fiscal Year")
plt.ylabel("Revenue ($ millions)")
plt.tight_layout()

plt.savefig("revenue_forecast.png", dpi=300, bbox_inches="tight")
plt.close()
print("\nChart saved as revenue_forecast.png")
