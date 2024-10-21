import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import logging
from src.ai.ai_helpers import PredictionHelper

# Initialize logger
logger = logging.getLogger(__name__)

class DNNModel:
    """
    Deep Neural Network (DNN) model for predictive trading.
    Trained on historical price data to make market predictions.
    """

    def __init__(self, input_shape, epochs=10, batch_size=32):
        """
        Initialize the DNN model with specified input shape, epochs, and batch size.
        """
        self.input_shape = input_shape
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self._build_model()
        self.prediction_helper = PredictionHelper()

    def _build_model(self):
        """
        Builds a simple feed-forward neural network (DNN).
        """
        model = Sequential()
        model.add(Dense(128, input_shape=self.input_shape, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))  # Single output for regression (e.g., price prediction)
        model.compile(optimizer='adam', loss='mean_squared_error')
        logger.info("DNN model architecture built.")
        return model

    def train(self, X_train, y_train):
        """
        Train the DNN model using historical data.
        """
        logger.info("Training DNN model...")
        self.model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batch_size)
        logger.info("DNN model training completed.")

    def predict(self, X):
        """
        Make price predictions based on input features.
        """
        predictions = self.model.predict(X)
        refined_predictions = self.prediction_helper.refine_predictions(predictions)
        logger.info(f"DNN model predictions made: {refined_predictions}")
        return refined_predictions

    def update_with_real_time_data(self, real_time_data, y_real_time):
        """
        Update the model with real-time data to improve predictions continuously.
        """
        self.model.fit(real_time_data, y_real_time, epochs=1, verbose=0)
        logger.info("DNN model updated with real-time data.")
