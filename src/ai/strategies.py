# File: /src/ai/strategies.py

import time
import logging
from src.trading.trade_executor import execute_trade
from arbitrage.triangle_arbitrage import execute_triangle_arbitrage
from arbitrage.cross_chain_arbitrage import execute_cross_chain_arbitrage
from wallets.wallet_manager import WalletManager
from src.database import insert_greenlist_log, get_greenlist

def prioritize_greenlist(asset_address, duration, wallet_manager: WalletManager):
    """
    Prioritize trading and accumulation for Greenlist assets.
    This function ensures that the AI focuses on accumulating a specific asset for
    a certain duration using advanced trading strategies like DCA, arbitrage, and liquidity management.

    Parameters:
    - asset_address (str): The address of the Greenlist asset.
    - duration (int): The time in minutes to focus on this asset.
    - wallet_manager (WalletManager): The WalletManager instance for dynamic wallet operations.
    
    Returns:
    - None
    """
    start_time = time.time()
    logging.info(f"Starting Greenlist priority for asset {asset_address} for {duration} minutes.")

    while (time.time() - start_time) < (duration * 60):
        # Step 1: Use aggressive DCA (Dollar-Cost Averaging) to accumulate Greenlist assets
        apply_dca_strategy(asset_address, wallet_manager)

        # Step 2: Execute arbitrage strategies (cross-chain, triangle) for Greenlist accumulation
        execute_triangle_arbitrage(asset_address)
        execute_cross_chain_arbitrage(asset_address)

        # Step 3: Log Greenlist-focused trades into the database for tracking
        insert_greenlist_log(asset_address, 'executed_trade', time.time())

        # Pause briefly between trades to avoid triggering detection by bots/mempool watchers
        time.sleep(15)  # Adjust as needed for production performance and stealth

    logging.info(f"Completed Greenlist priority for asset {asset_address}.")

def apply_dca_strategy(asset_address, wallet_manager: WalletManager):
    """
    Apply Dollar-Cost Averaging (DCA) strategy to accumulate Greenlist assets.
    The DCA strategy minimizes risk and market impact by buying in small increments over time.

    Parameters:
    - asset_address (str): The contract/token address of the Greenlist asset.
    - wallet_manager (WalletManager): The WalletManager instance for dynamic trade execution.
    
    Returns:
    - None
    """
    available_balance = wallet_manager.get_available_balance(asset_address)

    # Trade size is a small percentage of the available balance to avoid large market impact
    trade_size = available_balance * 0.01  # Example: 1% of balance
    logging.info(f"Executing DCA trade for {asset_address} with trade size: {trade_size:.8f}")
    
    # Execute the trade using trade_executor
    execute_trade(asset_address, trade_size)

def apply_greenlist_logic(wallet_manager: WalletManager):
    """
    Applies Greenlist logic by prioritizing Greenlist assets in trading strategies.
    Fetches Greenlist assets from the database and executes prioritization for each asset.

    Parameters:
    - wallet_manager (WalletManager): The WalletManager instance for dynamic trade execution.
    
    Returns:
    - None
    """
    greenlist_assets = get_greenlist()
    
    for asset in greenlist_assets:
        logging.info(f"Processing Greenlist asset: {asset['asset_address']}")
        prioritize_greenlist(asset["asset_address"], asset["focus_duration"], wallet_manager)
