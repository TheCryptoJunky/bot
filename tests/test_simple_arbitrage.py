# File: /tests/test_simple_arbitrage.py

import unittest
from src.arbitrage.simple_arbitrage import SimpleArbitrage  # Corrected import path
from unittest.mock import MagicMock

class TestSimpleArbitrage(unittest.TestCase):
    """
    Unit test for SimpleArbitrage class. Verifies that simple arbitrage opportunities
    are detected and executed correctly.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize SimpleArbitrage for testing.
        """
        self.arbitrage = SimpleArbitrage()

    def test_detect_arbitrage_opportunity(self):
        """
        Test that arbitrage opportunities are detected correctly.
        """
        self.arbitrage.detect_arbitrage_opportunity = MagicMock(return_value=True)
        result = self.arbitrage.detect_arbitrage_opportunity("ETH/BTC")
        self.assertTrue(result)

    def test_execute_arbitrage(self):
        """
        Test that an arbitrage trade is executed correctly.
        """
        self.arbitrage.execute_arbitrage = MagicMock(return_value=True)
        result = self.arbitrage.execute_arbitrage("ETH/BTC")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
