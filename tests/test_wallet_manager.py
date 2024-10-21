# File: /tests/test_wallet_manager.py

import unittest
from src.wallets.wallet_monitor import WalletMonitor  # Corrected import path

class TestWalletManager(unittest.TestCase):
    """
    Unit test for WalletManager. Verifies that wallet balances are monitored 
    and wallet transactions are handled correctly.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize WalletMonitor for testing.
        """
        self.wallet_monitor = WalletMonitor()

    def test_get_wallet_balance(self):
        """
        Test fetching the balance of a wallet.
        """
        balance = self.wallet_monitor.get_wallet_balance("0x12345")
        self.assertIsNotNone(balance)

    def test_track_wallet_transactions(self):
        """
        Test tracking wallet transactions.
        """
        transactions = self.wallet_monitor.track_wallet_transactions("0x12345")
        self.assertIsInstance(transactions, list)

if __name__ == '__main__':
    unittest.main()
