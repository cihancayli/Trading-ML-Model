from data_fetcher import fetch_spy_data, preprocess_data
from feature_engineering import add_technical_indicators
from model_training import train_model
from trading import create_alpaca_api, execute_trade

def main():
    raw_data = fetch_spy_data()
    processed_data = preprocess_data(raw_data)
    
    data_with_features = add_technical_indicators(processed_data)
    
    model = train_model(data_with_features, target_column='Close')

    signal = get_trading_signal(model, data_with_features)

    API_KEY = XXXX
    API_SECRET = YYYY
    BASE_URL = 'https://paper-api.alpaca.markets'
    api = create_alpaca_api(API_KEY, API_SECRET, BASE_URL)

    execute_trade(api, 'SPY', signal, quantity=1)

if __name__ == "__main__":
    main()
