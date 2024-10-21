# File: /tests/test_strategies.py

import unittest
from unittest.mock import MagicMock
from ai.strategies import prioritize_greenlist, apply_dca_strategy
from wallets.wallet_manager import WalletManager

class TestStrategies(unittest.TestCase):
    def setUp(self):
        self.wallet_manager = WalletManager()
        self.wallet_manager.get_available_balance = MagicMock(return_value=1000)  # Mock balance

    def test_prioritize_greenlist(self):
        """
        Test prioritizing Greenlist asset and ensuring DCA strategy is applied.
        """
        prioritize_greenlist("0xTestAsset123", 1, self.wallet_manager)
        self.wallet_manager.get_available_balance.assert_called_with("0xTestAsset123")

    def test_apply_dca_strategy(self):
        """
        Test the DCA strategy to ensure it's applied properly for a Greenlist asset.
        """
        apply_dca_strategy("0xTestAsset123", self.wallet_manager)
        self.wallet_manager.get_available_balance.assert_called_with("0xTestAsset123")

if __name__ == "__main__":
    unittest.main()
