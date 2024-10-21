# File: /src/ai/models/arima_model.py

from statsmodels.tsa.arima.model import ARIMA

class ARIMAModel:
    """
    ARIMA Model used for time-series prediction in the trading bot.
    """
    
    def __init__(self, order=(5, 1, 0)):
        """
        Initialize the ARIMA model with the specified order.
        
        :param order: The order of the ARIMA model (p, d, q).
        """
        self.model = None
        self.model_fit = None
        self.order = order

    def train(self, data):
        """
        Train the ARIMA model using the provided data.
        
        :param data: The time-series data for training.
        :return: Fitted model
        """
        # Initialize the ARIMA model with the provided data
        self.model = ARIMA(data, order=self.order)
        
        # Fit the model to the data (removed the 'disp=0' parameter)
        self.model_fit = self.model.fit()  # Updated fix
        
        return self.model_fit

    def predict(self, steps=5):
        """
        Make future predictions based on the fitted model.
        
        :param steps: Number of steps to predict into the future.
        :return: Predicted values
        """
        if not self.model_fit:
            raise ValueError("The model must be trained before making predictions.")
        
        # Predict future steps based on the trained model
        return self.model_fit.forecast(steps=steps)
