# File: /tests/test_settings_gui.py

import unittest
from unittest.mock import patch
import tkinter as tk
from gui.settings_gui import SettingsGUI

class TestSettingsGUI(unittest.TestCase):
    @patch("gui.settings_gui.save_settings")
    def test_save_settings(self, mock_save_settings):
        """
        Test saving settings via the GUI.
        """
        root = tk.Tk()
        app = SettingsGUI(root)
        app.save_button.invoke()  # Simulate save button press
        mock_save_settings.assert_called_once()
        root.destroy()

    @patch("gui.settings_gui.load_settings")
    def test_load_settings(self, mock_load_settings):
        """
        Test loading settings via the GUI.
        """
        root = tk.Tk()
        app = SettingsGUI(root)
        mock_load_settings.assert_called_once()
        root.destroy()

if __name__ == "__main__":
    unittest.main()
