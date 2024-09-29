# src/data_analysis.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def analyze_data(data):
    """
    Perform analysis on the data. This can include statistical analysis and
    building predictive models.

    Args:
    data (DataFrame): The data to analyze.

    Returns:
    dict: A dictionary with analysis results and model metrics.
    """
    # Simple Linear Regression to predict future prices
    X = data[['daily_pct_change']]  # Predictor
    y = data['Close']  # Response

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predicting the test set results and calculating the accuracy
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)

    return {'model_accuracy': accuracy}

# Example usage:
if __name__ == "__main__":
    from data_processing import clean_data
    from data_collection import fetch_financial_data
    data = fetch_financial_data('AAPL')
    cleaned_data = clean_data(data)
    results = analyze_data(cleaned_data)
    print(results)