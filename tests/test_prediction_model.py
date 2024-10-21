# File: /tests/test_prediction_model.py

import unittest
from ai.models.prediction_model import PredictionModel

class TestPredictionModel(unittest.TestCase):
    def setUp(self):
        self.model = PredictionModel()

    def test_train_model(self):
        """
        Test training the prediction model.
        """
        result = self.model.train([[0.1, 0.2], [0.2, 0.3]], [1, 0])
        self.assertTrue(result['success'])

    def test_predict(self):
        """
        Test making predictions with the model.
        """
        result = self.model.predict([[0.1, 0.2]])
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
