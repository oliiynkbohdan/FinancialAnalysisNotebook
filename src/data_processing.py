# src/data_processing.py

import pandas as pd

def clean_data(data):
    """
    Clean and prepare data for analysis. This can include removing null values,
    filtering columns, and adding new calculated columns.
    Args:
    data (DataFrame): The DataFrame to clean.

    Returns:
    DataFrame: The cleaned DataFrame.
    """
    # Remove any rows with missing data
    cleaned_data = data.dropna()
    
    # Example of adding a new feature: daily price change percentage
    cleaned_data['daily_pct_change'] = cleaned_data['Close'].pct_change() * 100
    cleaned_data = cleaned_data.dropna()  # Remove rows created by pct_change that have NaN
    
    return cleaned_data

# Example usage:
if __name__ == "__main__":
    from data_collection import fetch_financial_data
    data = fetch_financial_data('AAPL')
    cleaned_data = clean_data(data)
    print(cleaned_data.head())