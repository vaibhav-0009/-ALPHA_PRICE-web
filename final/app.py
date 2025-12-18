import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

# User inputs
stock_name = input("Enter the stock ticker symbol (e.g., GOOGL, AAPL): ").strip().upper()
today = datetime.today()

# Calculate the start date for the last 30 days
start_date = (today - timedelta(days=30)).strftime('%Y-%m-%d')

# End date is today
end_date = today.strftime('%Y-%m-%d')

# Fetch stock data
print(f"Fetching data for {stock_name} from {start_date} to {end_date}...")
data = yf.download(stock_name, start=start_date, end=end_date, progress=False)  # Daily-level data

# Fetch company details
ticker = yf.Ticker(stock_name)
company_name = ticker.info.get("longName", "N/A")
sector = ticker.info.get("sector", "N/A")
current_price = ticker.history(period="1d")['Close'][-1] if not ticker.history(period="1d").empty else "N/A"

# Check if data is empty
if data.empty:
    print("No data found for the specified stock and date range. Please try again.")
else:
    print(f"Company Name: {company_name}")
    print(f"Sector: {sector}")
    print(f"Current Price: ${current_price:.2f}" if current_price != "N/A" else "Current Price: N/A")

    # Prepare data for prediction
    data['Timestamp'] = data.index.map(datetime.timestamp)
    X = np.array(data['Timestamp']).reshape(-1, 1)  # Timestamps as features
    y = data['Close'].values  # Closing prices as target

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict future prices (e.g., next 30 days)
    future_dates = [data.index[-1] + timedelta(days=i) for i in range(1, 31)]
    future_timestamps = [date.timestamp() for date in future_dates]
    future_timestamps = np.array(future_timestamps).reshape(-1, 1)
    future_prices = model.predict(future_timestamps)

    # Plotting the actual and predicted prices
    plt.figure(figsize=(12, 6))  # Set figure size
    plt.plot(data.index, data['Close'], marker='o', label=f"{stock_name} Actual Closing Prices", color='blue')
    plt.plot(future_dates, future_prices, marker='x', label=f"{stock_name} Predicted Prices (Next 30 Days)", color='red')

    # Formatting the X-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Date format
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))  # Show every 3rd day

    # Rotating the dates for better readability
    plt.xticks(rotation=45)

    # Adding titles and labels
    plt.title(f'{company_name} ({stock_name}) Stock Prices and Predictions (Daily)', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Close Price (USD)', fontsize=12)
    plt.grid(True)
    plt.legend()

    # Show the graph
    plt.tight_layout()  # Adjust layout to fit everything
    plt.show()

    # Print predicted prices
    print("\nPredicted Prices for the Next 30 Days:")
    for date, price in zip(future_dates, future_prices):
        print(f"{date.strftime('%Y-%m-%d')}: ${price:.2f}")
