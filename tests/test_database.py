# File: /tests/test_database.py

import unittest
from src.database import insert_greenlist_log, get_greenlist, add_to_greenlist, remove_from_greenlist  # Corrected import path

class TestDatabase(unittest.TestCase):
    """
    Unit test for database interactions. Verifies that functions like adding to the greenlist,
    removing from it, and logging are working correctly.
    """

    def setUp(self):
        """
        Set up the test environment. Mock database connections for testing.
        """
        self.mock_data = {
            'asset': 'ETH',
            'priority': 1
        }

    def test_insert_greenlist_log(self):
        """
        Test that inserting into the greenlist log works correctly.
        """
        result = insert_greenlist_log(self.mock_data)
        self.assertTrue(result)

    def test_add_to_greenlist(self):
        """
        Test that assets are correctly added to the greenlist.
        """
        result = add_to_greenlist(self.mock_data)
        self.assertTrue(result)

    def test_remove_from_greenlist(self):
        """
        Test that assets are correctly removed from the greenlist.
        """
        result = remove_from_greenlist('ETH')
        self.assertTrue(result)

    def test_get_greenlist(self):
        """
        Test that the greenlist can be fetched from the database.
        """
        greenlist = get_greenlist()
        self.assertIsInstance(greenlist, list)

if __name__ == '__main__':
    unittest.main()
