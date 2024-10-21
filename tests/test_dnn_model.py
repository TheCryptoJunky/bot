# File: /tests/test_dnn_model.py

import unittest
from ai.models.dnn_model import DNNModel

class TestDNNModel(unittest.TestCase):
    def setUp(self):
        """
        Set up a new DNNModel for testing.
        """
        self.model = DNNModel()

    def test_train(self):
        """
        Test training the DNN model.
        """
        result = self.model.train([[0.1, 0.2], [0.2, 0.3]], [1, 0])
        self.assertTrue(result['success'])

    def test_predict(self):
        """
        Test making predictions with the DNN model.
        """
        result = self.model.predict([[0.1, 0.2]])
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
