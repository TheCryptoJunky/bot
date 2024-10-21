# File: /tests/test_lstm_model.py

import unittest
import numpy as np
from src.ai.models.lstm_model import LSTMModel  # Corrected import path

class TestLSTMModel(unittest.TestCase):
    """
    Unit test for the LSTM Model. Verifies that the model can be trained 
    and make predictions.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize the LSTMModel for testing.
        """
        self.input_shape = (60, 1)  # Example input shape
        self.lstm_model = LSTMModel(input_shape=self.input_shape)

    def test_model_build(self):
        """
        Test that the model builds correctly.
        """
        self.assertIsNotNone(self.lstm_model.model)
        self.assertEqual(len(self.lstm_model.model.layers), 4)  # 2 LSTM layers, 2 Dense layers

    def test_train(self):
        """
        Test training the LSTM model with mock data.
        """
        train_data = np.random.rand(100, 60, 1)  # 100 samples, 60 time steps, 1 feature
        train_labels = np.random.rand(100, 1)
        self.lstm_model.train(train_data, train_labels)
        self.assertIsNotNone(self.lstm_model.model)

    def test_predict(self):
        """
        Test making predictions with the LSTM model.
        """
        test_data = np.random.rand(10, 60, 1)  # 10 samples
        predictions = self.lstm_model.predict(test_data)
        self.assertEqual(predictions.shape, (10, 1))  # Ensure the correct output shape

if __name__ == '__main__':
    unittest.main()
