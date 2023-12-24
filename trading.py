import alpaca_trade_api as tradeapi

def create_alpaca_api(api_key, api_secret, base_url):
    """
    Creates an Alpaca API object.

    api_key (str):  Alpaca API key.
    api_secret (str):  Alpaca API secret.
    base_url (str): Alpaca's base URL for API calls.

    Returns:
    tradeapi.REST: The Alpaca API object.
    """
    api = tradeapi.REST(api_key, api_secret, base_url)
    return api

def execute_trade(api, symbol, signal, quantity):
    """
    Executes a trade on Alpaca based on the signal.

    api (tradeapi.REST): The Alpaca API object.
    symbol (str): The stock symbol to trade.
    signal (str): 'buy' or 'sell'.
    quantity (int): The number of shares to trade.
    """
    if signal == 'buy':
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif signal == 'sell':
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side='sell',
            type='market',
            time_in_force='gtc'
        )

# Sample usage
if __name__ == "__main__":
    API_KEY = 'XXXX'
    API_SECRET = 'YYYY'
    BASE_URL = 'https://paper-api.alpaca.markets'  #paper trading URL for testing

    # Create API object
    api = create_alpaca_api(XXXX,YYYY,ZZZZ)

    #Example trade
    execute_trade(api, 'SPY', 'buy', 1)
