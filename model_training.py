import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

def train_model(data, target_column='Close', test_size=0.2):
    """
    Trains a LightGBM model on the given dataset.

    Args:
    data (pandas.DataFrame): The dataset, including features and target.
    target_column (str): The name of the target variable column.
    test_size (float): Proportion of the dataset to include in the test split.

    Returns:
    lightgbm.Booster: The trained LightGBM model.
    """
    # Splitting the data into features and target
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # Create and train the LightGBM model
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)

    # Predict and evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    return model

# Sample usage
if __name__ == "__main__":
    # Load and preprocess data from previous steps
    # data = fetch_spy_data()
    # data = preprocess_data(data)
    # data = add_technical_indicators(data)

    # Train the model
    model = train_model(data)
