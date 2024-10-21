import statsmodels.api as sm

class TrendForecaster:
    def __init__(self, historical_data):
        self.historical_data = historical_data

    def forecast_trend(self, steps=10):
        """Uses ARIMA to forecast future trends based on historical data."""
        model = sm.tsa.ARIMA(self.historical_data, order=(5,1,0))
        model_fit = model.fit(disp=0)
        return model_fit.forecast(steps=steps)[0]
