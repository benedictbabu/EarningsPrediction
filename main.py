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
