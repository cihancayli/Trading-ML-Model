import talib

def add_technical_indicators(data):
    """
    Adds technical indicators as new features to the dataset.

    Args:
    data (pandas.DataFrame): The data with at least 'Close' prices.

    Returns:
    pandas.DataFrame: Data with added technical indicators.
    """
    #Simple Moving Average (SMA)
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)

    data['RSI'] = talib.RSI(data['Close'])

    # Other indicators can be added here as needed

    return data

if __name__ == "__main__":
    data = fetch_spy_data() 
    data = preprocess_data(data)
    data_with_indicators = add_technical_indicators(data)
    print(data_with_indicators.head())  # Display the first few rows with indicators
