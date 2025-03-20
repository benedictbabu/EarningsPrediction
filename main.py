import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define stock symbol, indices, and macroeconomic indicators
assets = {
    "MSFT": "Microsoft",
    "^GSPC": "S&P 500",
    "^NDX": "Nasdaq-100"
}
macro_indicators = {
    "FEDFUNDS": "Fed Funds Rate",
    "CPIAUCSL": "Inflation (CPI)"
}
start_date = "2020-03-01"
end_date = "2025-03-01"

# Fetch historical data for stocks and indices
data = {}
for ticker, name in assets.items():
    df = yf.download(ticker, start=start_date, end=end_date)[['Close']]
    df.rename(columns={'Close': name}, inplace=True)
    data[name] = df

# Fetch macroeconomic indicators from FRED
macro_data = pdr.DataReader(list(macro_indicators.keys()), 'fred', start_date, end_date)
macro_data.rename(columns=macro_indicators, inplace=True)

# Combine data into a single DataFrame
df_combined = pd.concat(data.values(), axis=1)
df_combined = df_combined.join(macro_data, how="outer")

# Calculate Moving Averages for Microsoft
df_combined["50-Day MA"] = df_combined["Microsoft"].rolling(window=50).mean()
df_combined["200-Day MA"] = df_combined["Microsoft"].rolling(window=200).mean()

# Normalize prices (Starting value = 100 for easy comparison)
df_normalized = df_combined / df_combined.iloc[0] * 100

# Plot Stock & Market Indices Performance
plt.figure(figsize=(12,6))
plt.plot(df_normalized.index, df_normalized["Microsoft"], label="Microsoft", color='blue', linewidth=1.5)
plt.plot(df_normalized.index, df_normalized["S&P 500"], label="S&P 500", color='black', linestyle="dashed")
plt.plot(df_normalized.index, df_normalized["Nasdaq-100"], label="Nasdaq-100", color='purple', linestyle="dashed")
plt.plot(df_normalized.index, df_normalized["50-Day MA"], label="MSFT 50-Day MA", color='red', linestyle="dotted")
plt.plot(df_normalized.index, df_normalized["200-Day MA"], label="MSFT 200-Day MA", color='green', linestyle="dotted")

# Formatting the plot
plt.title("Microsoft vs. Market Indices (S&P 500 & Nasdaq-100)", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Normalized Price (Base 100)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Plot Macroeconomic Indicators
fig, ax1 = plt.subplots(figsize=(12,6))

# Plot Fed Funds Rate (Interest Rate)
ax1.plot(macro_data.index, macro_data["Fed Funds Rate"], label="Fed Funds Rate", color='orange', linewidth=2)
ax1.set_ylabel("Interest Rate (%)", fontsize=12, color='orange')

# Create second y-axis for CPI
ax2 = ax1.twinx()
ax2.plot(macro_data.index, macro_data["Inflation (CPI)"], label="Inflation (CPI)", color='brown', linewidth=2)
ax2.set_ylabel("CPI (Indexed)", fontsize=12, color='brown')

# Formatting the plot
ax1.set_title("Macroeconomic Indicators: Interest Rate & Inflation", fontsize=14)
ax1.set_xlabel("Date", fontsize=12)
ax1.grid(True)
fig.legend(loc="upper left")
plt.show()
