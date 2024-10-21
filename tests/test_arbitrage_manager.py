# File: /tests/test_arbitrage_manager.py

import unittest
from src.arbitrage_manager import ArbitrageManager  # Corrected import path to match actual structure

class TestArbitrageManager(unittest.TestCase):
    """
    Unit test for the ArbitrageManager class. Verifies that arbitrage operations
    are correctly executed and managed by the ArbitrageManager.
    """

    def setUp(self):
        """
        Set up the test environment. Create an instance of the ArbitrageManager
        for testing purposes.
        """
        self.arbitrage_manager = ArbitrageManager()

    def test_initialization(self):
        """
        Test that the ArbitrageManager is initialized correctly.
        """
        self.assertIsNotNone(self.arbitrage_manager)
        self.assertEqual(self.arbitrage_manager.active_arbitrages, [])  # Ensure no arbitrages are active initially

    def test_add_arbitrage(self):
        """
        Test adding an arbitrage operation to the manager.
        """
        self.arbitrage_manager.add_arbitrage("ETH/BTC")
        self.assertIn("ETH/BTC", self.arbitrage_manager.active_arbitrages)

    def test_remove_arbitrage(self):
        """
        Test removing an arbitrage operation from the manager.
        """
        self.arbitrage_manager.add_arbitrage("ETH/BTC")
        self.arbitrage_manager.remove_arbitrage("ETH/BTC")
        self.assertNotIn("ETH/BTC", self.arbitrage_manager.active_arbitrages)

if __name__ == '__main__':
    unittest.main()
