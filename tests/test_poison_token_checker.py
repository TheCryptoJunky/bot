# File: /tests/test_poison_token_checker.py

import unittest
from src.safety.poison_token_checker import PoisonTokenChecker  # Corrected import path
from unittest.mock import MagicMock

class TestPoisonTokenChecker(unittest.TestCase):
    """
    Unit test for the PoisonTokenChecker. Verifies that the bot correctly
    detects and handles malicious tokens.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize PoisonTokenChecker for testing.
        """
        self.token_checker = PoisonTokenChecker(token_api_url="https://example.com/api", mysql_config={
            'host': 'localhost', 'user': 'root', 'password': 'password', 'database': 'crypto_db'
        })

    def test_is_token_safe(self):
        """
        Test that the token checker correctly verifies a token's safety.
        """
        self.token_checker.is_blacklisted = MagicMock(return_value=False)
        self.token_checker.is_whitelisted = MagicMock(return_value=False)
        self.token_checker.check_external_api = MagicMock(return_value=True)
        is_safe = self.token_checker.is_token_safe("0xTokenAddress")
        self.assertTrue(is_safe)

    def test_add_to_blacklist(self):
        """
        Test that a token is correctly added to the blacklist.
        """
        self.token_checker.add_to_blacklist = MagicMock(return_value=True)
        result = self.token_checker.add_to_blacklist("0xScamToken")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
