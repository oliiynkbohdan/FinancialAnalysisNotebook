# src/main.py

from data_collection import fetch_financial_data
from data_processing import clean_data
from data_analysis import analyze_data
from visualization import visualize_data

def main():
    """
    Main function to run the financial data analysis pipeline.
    """
    # Step 1: Fetch Data
    print("Fetching data...")
    data = fetch_financial_data('AAPL')  # You can parameterize the symbol as needed

    # Step 2: Process Data
    print("Processing data...")
    cleaned_data = clean_data(data)

    # Step 3: Analyze Data
    print("Analyzing data...")
    analysis_results = analyze_data(cleaned_data)

    # Step 4: Visualize Results
    print("Visualizing results...")
    visualize_data(cleaned_data)

    # Output Analysis Results
    print("Analysis Results:", analysis_results)

if __name__ == '__main__':
    main()