Here's an enhanced version of your script that includes moving averages (50-day & 200-day) along with the closing price. This will help in identifying trends and potential trading signals.

Features Added:
50-day Moving Average (Short-term Trend)
200-day Moving Average (Long-term Trend)
Improved Visualization

Updated Python Code:

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define stock symbol and date range
ticker = "MSFT"
start_date = "2020-03-01"
end_date = "2025-03-01"

# Fetch historical data
msft_data = yf.download(ticker, start=start_date, end=end_date)

# Save to CSV file
msft_data.to_csv("MSFT_Historical_Data.csv")

# Calculate Moving Averages
msft_data['50-Day MA'] = msft_data['Close'].rolling(window=50).mean()
msft_data['200-Day MA'] = msft_data['Close'].rolling(window=200).mean()

# Plot closing price with moving averages
plt.figure(figsize=(12,6))
plt.plot(msft_data.index, msft_data['Close'], label="MSFT Closing Price", color='blue', linewidth=1.5)
plt.plot(msft_data.index, msft_data['50-Day MA'], label="50-Day MA", color='red', linestyle="dashed")
plt.plot(msft_data.index, msft_data['200-Day MA'], label="200-Day MA", color='green', linestyle="dashed")

# Formatting the plot
plt.title("Microsoft (MSFT) Stock Price with Moving Averages (Last 5 Years)", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


What This Does:
Visualizes Microsoft’s stock price over the past 5 years.
Adds 50-day & 200-day moving averages to identify short-term & long-term trends.
Dashed lines help differentiate moving averages from the actual stock price.
