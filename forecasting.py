import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def simple_forecast(data, country, periods=30):
    """
    Simple forecasting using linear regression on recent trend
    """
    # Filter data for the specific country
    country_data = data[data['Country/Region'] == country].copy()
    
    if len(country_data) < 30:
        return None, None
    
    # Use the last 90 days for trend calculation
    recent_data = country_data.tail(90).reset_index(drop=True)
    
    # Create features for regression (using days as features)
    recent_data['Days'] = range(len(recent_data))
    
    # Prepare data for regression
    X = recent_data['Days'].values.reshape(-1, 1)
    y = recent_data['Confirmed'].values
    
    # Fit linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Create future predictions
    future_days = np.array(range(len(recent_data), len(recent_data) + periods)).reshape(-1, 1)
    future_predictions = model.predict(future_days)
    
    # Create future dates
    last_date = recent_data['Date'].iloc[-1]
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, periods+1)]
    
    # Calculate model performance metrics on recent data
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)
    
    metrics = {
        'MAE': mae,
        'RMSE': rmse,
        'R2': r2
    }
    
    # Create result DataFrame
    forecast_df = pd.DataFrame({
        'Date': future_dates,
        'Forecast': future_predictions
    })
    
    return forecast_df, metrics

# Test the function
if __name__ == "__main__":
    from data_loader import load_available_data
    
    data_dict = load_available_data()
    time_series_data = data_dict['time_series']
    
    forecast, metrics = simple_forecast(time_series_data, "US")
    if forecast is not None:
        print("Forecast for US:")
        print(forecast.head())
        print("\nModel Metrics:")
        print(metrics)
