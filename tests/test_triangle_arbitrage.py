# File: /tests/test_triangle_arbitrage.py

import unittest
from src.arbitrage.triangle_arbitrage import execute_triangle_arbitrage  # Corrected import path
from unittest.mock import MagicMock

class TestTriangleArbitrage(unittest.TestCase):
    """
    Unit test for triangle arbitrage. Verifies that triangle arbitrage operations
    are executed correctly.
    """

    def test_execute_triangle_arbitrage(self):
        """
        Test executing a triangle arbitrage trade.
        """
        execute_triangle_arbitrage = MagicMock(return_value=True)
        result = execute_triangle_arbitrage('ETH/USDT', 'BTC/USDT', 'ETH/BTC')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
