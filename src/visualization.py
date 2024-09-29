# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    """
    Visualize the data with plots.

    Args:
    data (DataFrame): The data to visualize.
    """
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=data.index, y=data['Close'])
    plt.title('Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.show()

# Example usage:
if __name__ == "__main__":
    from data_processing import clean_data
    from data_collection import fetch_financial_data
    data = fetch_financial_data('AAPL')
    cleaned_data = clean_data(data)
    visualize_data(cleaned_data)