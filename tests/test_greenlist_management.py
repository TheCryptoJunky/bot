# File: /tests/test_greenlist_management.py

import unittest
from unittest.mock import patch
from gui.greenlist_management import GreenlistManager
import tkinter as tk

class TestGreenlistManager(unittest.TestCase):
    @patch("gui.greenlist_management.add_to_greenlist")
    def test_add_asset(self, mock_add_to_greenlist):
        """
        Test adding an asset to the Greenlist via the GUI.
        """
        root = tk.Tk()
        app = GreenlistManager(root)
        app.asset_entry.insert(0, "0xTestAsset123")
        app.focus_entry.insert(0, "60")
        app.add_asset()
        mock_add_to_greenlist.assert_called_with("0xTestAsset123", 60)
        root.destroy()

    @patch("gui.greenlist_management.remove_from_greenlist")
    def test_remove_asset(self, mock_remove_from_greenlist):
        """
        Test removing an asset from the Greenlist via the GUI.
        """
        root = tk.Tk()
        app = GreenlistManager(root)
        app.greenlist_display.insert(0, "0xTestAsset123")
        app.greenlist_display.selection_set(0)
        app.remove_asset()
        mock_remove_from_greenlist.assert_called_with("0xTestAsset123")
        root.destroy()

if __name__ == "__main__":
    unittest.main()
