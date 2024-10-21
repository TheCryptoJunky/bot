# File: /tests/test_liquidity_provision_bot.py

import sys
import os
import unittest
from unittest.mock import MagicMock
from src.advanced_arbitrage.liquidity_provision_arbitrage_bot import LiquidityProvisionArbitrageBot

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLiquidityProvisionArbitrageBot(unittest.TestCase):
    """
    Unit tests for the LiquidityProvisionArbitrageBot.
    Ensures correct execution of liquidity provision arbitrage using mock exchanges and RL agent.
    """

    def setUp(self):
        # Set up the bot and mock dependencies
        self.config = {'symbols': ['BTC/USDT', 'ETH/USDT']}
        self.bot = LiquidityProvisionArbitrageBot(self.config)

        # Mock exchanges, RL agent, and safety mechanisms
        self.bot.exchange1 = MagicMock()
        self.bot.exchange2 = MagicMock()
        self.bot.rl_agent = MagicMock()

    def test_liquidity_provision_arbitrage(self):
        """
        Test the execution of liquidity provision arbitrage with mocked exchange data and RL agent decisions.
        """
        # Mock price data for both exchanges
        self.bot.exchange1.fetch_ticker.return_value = {'last': 3000}
        self.bot.exchange2.fetch_ticker.return_value = {'last': 3050}

        # Mock RL agent's decision-making
        self.bot.rl_agent.choose_action.return_value = "buy_on_1_sell_on_2"

        # Mock trade execution
        self.bot._execute_arbitrage = MagicMock()

        # Run the arbitrage logic
        self.bot.analyze_and_trade('BTC/USDT', 1000000)
        self.bot._execute_arbitrage.assert_called()

if __name__ == '__main__':
    unittest.main()
