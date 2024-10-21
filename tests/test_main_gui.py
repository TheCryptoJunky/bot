# File: /tests/test_main_gui.py

import unittest
from unittest.mock import patch
import tkinter as tk
from gui.main_gui import MainGUI

class TestMainGUI(unittest.TestCase):
    @patch("gui.main_gui.run_arbitrage")
    def test_run_arbitrage(self, mock_run_arbitrage):
        """
        Test triggering arbitrage from the main GUI.
        """
        root = tk.Tk()
        app = MainGUI(root)
        app.run_arbitrage()
        mock_run_arbitrage.assert_called_once()
        root.destroy()

    @patch("gui.main_gui.show_trade_history")
    def test_show_trade_history(self, mock_show_trade_history):
        """
        Test displaying trade history from the main GUI.
        """
        root = tk.Tk()
        app = MainGUI(root)
        app.show_trade_history()
        mock_show_trade_history.assert_called_once()
        root.destroy()

if __name__ == "__main__":
    unittest.main()
