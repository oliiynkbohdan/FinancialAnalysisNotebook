# src/data_collection.py

import yfinance as yf

def fetch_financial_data(symbol):
    """
    Fetch financial data for a given stock symbol using Yahoo Finance.

    Args:
    symbol (str): Stock symbol to fetch data for (e.g., 'AAPL' for Apple Inc.).

    Returns:
    DataFrame: Historical market data.
    """
    stock = yf.Ticker(symbol)
    data = stock.history(period="max")  # You can customize the period e.g., '1mo', '1y', '5y', 'max'
    return data

# Example usage:
if __name__ == "__main__":
    symbol = 'AAPL'  # Example: Apple Inc.
    data = fetch_financial_data(symbol)
    print(data.head())  # Print the first few rows of the data