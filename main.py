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

# Plot closing price
plt.figure(figsize=(12,6))
plt.plot(msft_data.index, msft_data['Close'], label="MSFT Closing Price", color='blue')

# Formatting the plot
plt.title("Microsoft (MSFT) Stock Closing Price (Last 5 Years)", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Closing Price (USD)", fontsize=12)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
