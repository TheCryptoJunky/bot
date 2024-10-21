import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

class AIModel:
    def __init__(self, input_shape):
        self.model = self._build_model(input_shape)

    def _build_model(self, input_shape):
        """Builds an LSTM model for market prediction."""
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
        model.add(LSTM(50))
        model.add(Dense(1))  # Predict a single value (e.g., next price)
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=64):
        """Trains the model on historical data."""
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, X):
        """Makes predictions based on input data."""
        return self.model.predict(X)

    def update_with_real_time_data(self, real_time_data, y_real_time):
        """Updates the model with real-time data to retrain it periodically."""
        self.model.fit(real_time_data, y_real_time, epochs=1, verbose=0)
