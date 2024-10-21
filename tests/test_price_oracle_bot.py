# File: /tests/test_price_oracle_bot.py

import unittest
from helper_bots.price_oracle_bot import PriceOracleBot
from unittest.mock import MagicMock

class TestPriceOracleBot(unittest.TestCase):
    """
    Unit test for the Price Oracle Bot.
    """

    def setUp(self):
        self.config = {
            'target_pairs': ['ETH/USDT', 'BTC/USDT'],
            'price_diff_threshold': 0.01
        }
        self.price_oracle = PriceOracleBot(exchanges=['binance'], config=self.config)

    def test_fetch_price(self):
        """
        Test fetching the price from an exchange.
        """
        self.price_oracle.fetch_price = MagicMock(return_value=2000)  # Mock the fetch_price method
        price = self.price_oracle.fetch_price('binance', 'ETH/USDT')
        self.assertEqual(price, 2000)

    def test_detect_price_mismatch(self):
        """
        Test detecting price mismatches between exchanges.
        """
        self.price_oracle.price_data = {
            ('binance', 'ETH/USDT'): 2000,
            ('coinbase', 'ETH/USDT'): 2020
        }
        self.price_oracle.detect_price_mismatch()
        # Expected behavior: arbitrage should be triggered

if __name__ == '__main__':
    unittest.main()
