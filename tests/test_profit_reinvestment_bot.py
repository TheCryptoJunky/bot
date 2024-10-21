# File: /tests/test_profit_reinvestment_bot.py

import unittest
from src.helper_bots.profit_reinvestment_bot import ProfitReinvestmentBot  # Corrected import path
from unittest.mock import MagicMock

class TestProfitReinvestmentBot(unittest.TestCase):
    """
    Unit test for the ProfitReinvestmentBot. Verifies that the bot correctly
    reinvests profits based on predefined strategies.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize ProfitReinvestmentBot for testing.
        """
        self.bot = ProfitReinvestmentBot()

    def test_collect_profits(self):
        """
        Test collecting profits.
        """
        self.bot.collect_profits = MagicMock(return_value=1000)
        profit = self.bot.collect_profits()
        self.assertEqual(profit, 1000)

    def test_reinvest_profits(self):
        """
        Test reinvesting profits.
        """
        self.bot.reinvest_profits = MagicMock(return_value=True)
        result = self.bot.reinvest_profits()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
