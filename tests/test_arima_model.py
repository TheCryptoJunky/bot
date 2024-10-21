# File: /tests/test_arima_model.py

import unittest
from src.ai.models.arima_model import ARIMAModel  # Corrected import path

class TestARIMAModel(unittest.TestCase):
    """
    Unit test for the ARIMAModel class. Verifies that the ARIMA model is 
    correctly initialized, trained, and can make predictions.
    """

    def setUp(self):
        """
        Set up the test environment. Create an instance of ARIMAModel for testing purposes.
        """
        self.arima_model = ARIMAModel(p=5, d=1, q=0)

    def test_initialization(self):
        """
        Test that the ARIMAModel is initialized with the correct parameters.
        """
        self.assertEqual(self.arima_model.p, 5)
        self.assertEqual(self.arima_model.d, 1)
        self.assertEqual(self.arima_model.q, 0)

    def test_train(self):
        """
        Test training the ARIMAModel with mock data.
        """
        mock_data = [100, 102, 103, 101, 99]  # Example time series data
        self.arima_model.train(mock_data)
        self.assertIsNotNone(self.arima_model.model)  # Ensure model is trained

    def test_predict(self):
        """
        Test making predictions with the trained ARIMAModel.
        """
        mock_data = [100, 102, 103, 101, 99]  # Example time series data
        self.arima_model.train(mock_data)
        prediction = self.arima_model.predict(steps=5)
        self.assertEqual(len(prediction), 5)  # Ensure we get the correct number of predictions

if __name__ == '__main__':
    unittest.main()
