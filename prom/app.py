from flask import Flask, render_template, request, send_file
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    graph_path = None  # Initialize graph path
    if request.method == "POST":
        # Get stock ticker from the form
        stock_name = request.form.get("stock_name").upper()
        today = datetime.today()
        start_date = (today - timedelta(days=30)).strftime('%Y-%m-%d')
        end_date = today.strftime('%Y-%m-%d')

        # Fetch stock data
        data = yf.download(stock_name, start=start_date, end=end_date, progress=False)

        if data.empty:
            return render_template("indexgraph.html", error="No data found for the stock ticker. Please try again.")
        
        # Plot the stock data
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Close'], marker='o', label=stock_name, color='blue')
        plt.title(f'{stock_name} Stock Prices (Last 30 Days)', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Close Price (USD)', fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot
        graph_path = f"static/{stock_name}_graph.png"
        plt.savefig(graph_path)
        plt.close()  # Close the plot to free memory

    return render_template("indexgraph.html", graph_path=graph_path)

if __name__ == "__main__":
    app.run(debug=True)
