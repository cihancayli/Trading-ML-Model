import yfinance as yf
import pandas as pd

def fetch_spy_data(start_date='2000-01-01', end_date='2023-01-01'):
    """
    Fetches historical data for the SPY ETF.
    
    Args:
    start_date (str): Start date for fetching data in YYYY-MM-DD format.
    end_date (str): End date for fetching data in YYYY-MM-DD format.
    
    Returns:
    pandas.DataFrame: DataFrame containing historical prices.
    """
    data = yf.download('SPY', start=start_date, end=end_date)
    return data

def preprocess_data(data):
    """
    Basic preprocessing of the data.

    Args:
    data (pandas.DataFrame): The raw data.

    Returns:
    pandas.DataFrame: Preprocessed data.
    """
    # Handling missing values
    data = data.dropna()

    return data

if __name__ == "__main__":
    raw_data = fetch_spy_data()
    processed_data = preprocess_data(raw_data)
    print(processed_data.head())  # Display the first few rows
