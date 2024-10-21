# File: /src/ai/models/lstm_model.py

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
import logging
from src.ai.ai_helpers import PredictionHelper  # AI Helper for enhancing prediction accuracy
from centralized_logger import CentralizedLogger

# Initialize logger and centralized logging
logger = logging.getLogger(__name__)
centralized_logger = CentralizedLogger()

class LSTMModel:
    """
    A 5th-generation AI-driven LSTM model for predictive trading.
    This model forecasts future price movements based on historical data using Long Short-Term Memory neural networks.
    Optimized for low-latency predictions, integrated into the autonomous trading framework.
    """

    def __init__(self, input_shape, epochs=10, batch_size=32):
        """
        Initializes the LSTM model with the input shape, number of epochs, and batch size for training.
        """
        self.input_shape = input_shape
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self.build_model()  # Build the LSTM model
        self.prediction_helper = PredictionHelper()  # AI Helper for enhancing prediction accuracy

    def build_model(self):
        """
        Builds the LSTM model architecture using Keras.
        """
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=self.input_shape))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dense(25))
        model.add(Dense(1))  # Output layer for price prediction
        model.compile(optimizer='adam', loss='mean_squared_error')
        logger.info("LSTM model architecture built.")
        return model

    def train(self, train_data, train_labels):
        """
        Trains the LSTM model using the provided training data and labels.
        """
        logger.info("Training LSTM model...")
        self.model.fit(train_data, train_labels, epochs=self.epochs, batch_size=self.batch_size)
        logger.info("LSTM model training completed.")
        centralized_logger.log_event("LSTM model trained.")

    def predict(self, data):
        """
        Uses the trained LSTM model to predict future prices.
        Leverages AI Helper to improve prediction accuracy in real-time.
        """
        predictions = self.model.predict(data)
        # Enhance prediction accuracy using the AI Helper
        refined_predictions = self.prediction_helper.refine_predictions(predictions)
        logger.info(f"LSTM model predictions made: {refined_predictions}")
        return refined_predictions

    def save_model(self, path):
        """
        Saves the trained LSTM model to a file.
        """
        self.model.save(path)
        logger.info(f"LSTM model saved to {path}")

    def load_model(self, path):
        """
        Loads a pre-trained LSTM model from a file.
        """
        from keras.models import load_model
        self.model = load_model(path)
        logger.info(f"LSTM model loaded from {path}")
