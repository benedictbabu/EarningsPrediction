Modify the code to display Market Indices Data (e.g., S&P 500, Nasdaq-100) - Helps measure Microsoft's performance relative to the broader market.

Here’s an enhanced version of your script that includes market indices data (S&P 500 & Nasdaq-100). This will help you compare Microsoft’s stock price performance relative to the broader market.

New Features Added:
S&P 500 Index (^GSPC) 📊
Nasdaq-100 Index (^NDX) 📈
Normalized Prices for better comparison 📏
Moving Averages (50-day & 200-day) for Microsoft

Updated Python Code:

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define stock symbol and indices
assets = {
    "MSFT": "Microsoft",
    "^GSPC": "S&P 500",
    "^NDX": "Nasdaq-100"
}
start_date = "2020-03-01"
end_date = "2025-03-01"

# Fetch historical data for all assets
data = {}
for ticker, name in assets.items():
    df = yf.download(ticker, start=start_date, end=end_date)[['Close']]
    df.rename(columns={'Close': name}, inplace=True)
    data[name] = df

# Combine data into a single DataFrame
df_combined = pd.concat(data.values(), axis=1)

# Calculate Moving Averages for Microsoft
df_combined["50-Day MA"] = df_combined["Microsoft"].rolling(window=50).mean()
df_combined["200-Day MA"] = df_combined["Microsoft"].rolling(window=200).mean()

# Normalize prices (Starting value = 100 for easy comparison)
df_normalized = df_combined / df_combined.iloc[0] * 100

# Plot comparison
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

# Show the plot
plt.show()



import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define stock symbol and indices
assets = {
    "MSFT": "Microsoft",
    "^GSPC": "S&P 500",
    "^NDX": "Nasdaq-100"
}
start_date = "2020-03-01"
end_date = "2025-03-01"

# Fetch historical data for all assets
data = {}
for ticker, name in assets.items():
    df = yf.download(ticker, start=start_date, end=end_date)[['Close']]
    df.rename(columns={'Close': name}, inplace=True)
    data[name] = df

# Combine data into a single DataFrame
df_combined = pd.concat(data.values(), axis=1)

# Calculate Moving Averages for Microsoft
df_combined["50-Day MA"] = df_combined["Microsoft"].rolling(window=50).mean()
df_combined["200-Day MA"] = df_combined["Microsoft"].rolling(window=200).mean()

# Normalize prices (Starting value = 100 for easy comparison)
df_normalized = df_combined / df_combined.iloc[0] * 100

# Plot comparison
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

# Show the plot
plt.show()



import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define stock symbol and indices
assets = {
    "MSFT": "Microsoft",
    "^GSPC": "S&P 500",
    "^NDX": "Nasdaq-100"
}
start_date = "2020-03-01"
end_date = "2025-03-01"

# Fetch historical data for all assets
data = {}
for ticker, name in assets.items():
    df = yf.download(ticker, start=start_date, end=end_date)[['Close']]
    df.rename(columns={'Close': name}, inplace=True)
    data[name] = df

# Combine data into a single DataFrame
df_combined = pd.concat(data.values(), axis=1)

# Calculate Moving Averages for Microsoft
df_combined["50-Day MA"] = df_combined["Microsoft"].rolling(window=50).mean()
df_combined["200-Day MA"] = df_combined["Microsoft"].rolling(window=200).mean()

# Normalize prices (Starting value = 100 for easy comparison)
df_normalized = df_combined / df_combined.iloc[0] * 100

# Plot comparison
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

# Show the plot
plt.show()


What This Does:
Compares Microsoft's performance relative to the S&P 500 & Nasdaq-100.
Normalizes prices so they start at 100, making trends easier to compare.
Adds Moving Averages to show Microsoft's trend over time.
