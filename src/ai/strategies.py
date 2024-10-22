import time
import logging
from src.trading.trade_executor import execute_trade
from src.strategies.triangle_arbitrage import execute_triangle_arbitrage
from src.strategies.cross_chain_arbitrage import execute_cross_chain_arbitrage
from src.managers.wallet_manager import WalletManager
from src.database import insert_greenlist_log, get_greenlist

def prioritize_greenlist(asset_address, duration, wallet_manager: WalletManager):
    """
    Prioritize trading and accumulation for Greenlist assets using various strategies like DCA and arbitrage.
    Parameters:
    - asset_address (str): The address of the Greenlist asset.
    - duration (int): Time in minutes to focus on this asset.
    - wallet_manager (WalletManager): Wallet manager for dynamic wallet operations.
    """
    start_time = time.time()
    logging.info(f"Starting Greenlist priority for asset {asset_address} for {duration} minutes.")

    while (time.time() - start_time) < (duration * 60):
        apply_dca_strategy(asset_address, wallet_manager)
        execute_triangle_arbitrage(asset_address)
        execute_cross_chain_arbitrage(asset_address)
        insert_greenlist_log(asset_address, 'executed_trade', time.time())
        time.sleep(15)

    logging.info(f"Completed Greenlist priority for asset {asset_address}.")

def apply_dca_strategy(asset_address, wallet_manager: WalletManager):
    """Apply Dollar-Cost Averaging (DCA) strategy to accumulate Greenlist assets."""
    available_balance = wallet_manager.get_available_balance(asset_address)
    trade_size = available_balance * 0.01  # Trade 1% of balance
    logging.info(f"Executing DCA trade for {asset_address} with trade size: {trade_size:.8f}")
    execute_trade(asset_address, trade_size)

def apply_greenlist_logic(wallet_manager: WalletManager):
    """Apply Greenlist logic by prioritizing Greenlist assets in trading strategies."""
    greenlist_assets = get_greenlist()
    for asset in greenlist_assets:
        logging.info(f"Processing Greenlist asset: {asset['asset_address']}")
        prioritize_greenlist(asset["asset_address"], asset["focus_duration"], wallet_manager)
