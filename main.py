import asyncio
import os
from dotenv import load_dotenv
from src.managers.arbitrage_manager import ArbitrageManager
from src.managers.strategy_manager import StrategyManager
from src.managers.risk_manager import RiskManager
from src.managers.wallet_manager import WalletManager
from src.managers.transaction_manager import TransactionManager
from centralized_logger import CentralizedLogger
from src.utils.error_handler import handle_errors

# Load environment variables
load_dotenv()

# Initialize logger
logger = CentralizedLogger()

# Initialize the managers
arbitrage_manager = ArbitrageManager()
strategy_manager = StrategyManager()
risk_manager = RiskManager()
wallet_manager = WalletManager()
transaction_manager = TransactionManager()

async def initialize_bots():
    """
    Asynchronously initialize and start the bots, ensuring all managers and safety checks are in place.
    """
    try:
        # Ensure wallets and accounts are ready
        logger.log("info", "Initializing wallets...")
        await wallet_manager.initialize_wallets()

        # Load strategies from the strategy manager
        logger.log("info", "Loading trading strategies...")
        strategies = await strategy_manager.load_strategies()

        # Start arbitrage bots asynchronously
        logger.log("info", "Starting arbitrage bots...")
        await arbitrage_manager.start_arbitrage_bots(strategies)

        # Monitor risks and dynamically adjust bots using RiskManager
        logger.log("info", "Starting risk management...")
        await risk_manager.monitor_risks()

        # Log completion
        logger.log("info", "All bots started successfully.")

    except Exception as e:
        logger.log("error", f"Error while initializing bots: {str(e)}")
        handle_errors(e)

async def main():
    """
    Main entry point of the bot framework, coordinating the initialization and startup of bots.
    """
    logger.log("info", "Starting the bot framework...")

    # Initialize and start the bots
    await initialize_bots()

    # Keep running
    while True:
        await asyncio.sleep(3600)  # Keep the program running, can add a monitor loop here

# Entry point for the script
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.log("critical", f"Critical failure in main execution: {str(e)}")
