from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexstock.html')  # Renders the input form

@app.route('/result', methods=['POST'])
def result():
    stock_name = request.form['ticker'].strip().upper()  # Get user input
    try:
        # Fetch stock data using yfinance
        ticker = yf.Ticker(stock_name)

        # Company information
        company_name = ticker.info.get("longName", "N/A")
        sector = ticker.info.get("sector", "N/A")

        # Current stock price
        current_price = ticker.history(period="1d")['Close'][-1]

        # Pass data to the result page
        return render_template('result.html', stock_name=stock_name, company_name=company_name,
                               sector=sector, current_price=current_price)
    except Exception as e:
        # Handle errors gracefully
        error_message = f"Unable to fetch details for {stock_name}. Please check the ticker or try again."
        return render_template('result.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
