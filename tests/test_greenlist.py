# File: /tests/test_greenlist.py

import unittest
from database import add_to_greenlist, remove_from_greenlist, get_greenlist, update_focus_duration

class TestGreenlist(unittest.TestCase):
    def setUp(self):
        """
        Set up initial test state by clearing Greenlist before each test.
        """
        # Assuming we have a method to clear the greenlist for testing purposes
        clear_greenlist()

    def test_add_to_greenlist(self):
        """
        Test adding an asset to the Greenlist.
        """
        asset_address = "0xTestAsset123"
        focus_duration = 60  # 60 minutes

        add_to_greenlist(asset_address, focus_duration)
        greenlist = get_greenlist()

        self.assertEqual(len(greenlist), 1)
        self.assertEqual(greenlist[0]["asset_address"], asset_address)

    def test_remove_from_greenlist(self):
        """
        Test removing an asset from the Greenlist.
        """
        asset_address = "0xTestAsset123"
        focus_duration = 60

        add_to_greenlist(asset_address, focus_duration)
        remove_from_greenlist(asset_address)
        greenlist = get_greenlist()

        self.assertEqual(len(greenlist), 0)

    def test_update_focus_duration(self):
        """
        Test updating the focus duration of a Greenlist asset.
        """
        asset_address = "0xTestAsset123"
        initial_duration = 60
        new_duration = 120

        add_to_greenlist(asset_address, initial_duration)
        update_focus_duration(asset_address, new_duration)

        greenlist = get_greenlist()
        self.assertEqual(greenlist[0]["focus_duration"], new_duration)

if __name__ == "__main__":
    unittest.main()
