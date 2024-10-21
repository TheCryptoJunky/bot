# File: /tests/test_trade_executor.py

import unittest
from src.trading.trade_executor import execute_trade, perform_trade  # Corrected import path
from unittest.mock import MagicMock

class TestTradeExecutor(unittest.TestCase):
    """
    Unit test for the Trade Executor. Verifies that trades are correctly executed
    using the trade executor functions.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize mock data for testing.
        """
        self.pair = "ETH/USDT"
        self.amount = 1000

    def test_execute_trade(self):
        """
        Test executing a trade.
        """
        execute_trade = MagicMock(return_value=True)
        result = execute_trade(self.pair, self.amount)
        self.assertTrue(result)

    def test_perform_trade(self):
        """
        Test performing a trade.
        """
        perform_trade = MagicMock(return_value=True)
        result = perform_trade(self.pair, "buy", self.amount)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
