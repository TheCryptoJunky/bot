# File: /tests/test_transaction_manager.py

import unittest
from src.transaction_manager.transaction_manager import TransactionManager  # Corrected import path

class TestTransactionManager(unittest.TestCase):
    """
    Unit test for the TransactionManager class. Verifies that transactions are correctly
    processed and logged by the transaction manager.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize TransactionManager for testing.
        """
        self.transaction_manager = TransactionManager()

    def test_process_transaction(self):
        """
        Test that a transaction is processed correctly.
        """
        result = self.transaction_manager.process_transaction("0xSender", "0xReceiver", 1000, "ETH")
        self.assertTrue(result)

    def test_log_transaction(self):
        """
        Test that a transaction is logged correctly.
        """
        result = self.transaction_manager.log_transaction("0xSender", "0xReceiver", 1000, "ETH")
        self.assertTrue(result)

    def test_get_transaction_history(self):
        """
        Test that the transaction history is retrieved correctly.
        """
        history = self.transaction_manager.get_transaction_history("0xSender")
        self.assertIsInstance(history, list)

if __name__ == '__main__':
    unittest.main()
