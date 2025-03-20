# EarningsPrediction
Apply business analytics skills to predict stock returns for publicly traded companies in the next 30 days.

Use web scripting technology(Python) to retrieve relevant information
from available financial datasets, such as Yahoo Finance.
Gather data for the relevant variables of Microsoft over the past 5 years from
March 1, 2025. (e.g., https://uk.finance.yahoo.com/quote/MSFT/history/)

To gather historical financial data for Microsoft (MSFT) over the past 5 years from Yahoo Finance using Python, we can use the yfinance library. Below is a Python script to retrieve relevant data:

Steps:
Install the required library: pip install yfinance
Use yfinance to download historical stock prices.
Save the data to a CSV file for further analysis.

Python Script:

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


Explanation:
The script fetches daily stock prices (open, high, low, close, volume, adjusted close).
The data covers the period from March 1, 2020, to March 1, 2025.
The result is stored in a CSV file for further analysis.

Output:
This script will generate a line plot showing how Microsoft’s closing price has evolved over the last 5 years.
The plot is saved and displayed for further analysis.
The dataset is stored as "MSFT_Historical_Data.csv" for future reference.

