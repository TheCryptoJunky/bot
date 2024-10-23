import os
import json
from web3 import Web3
from datetime import datetime
from typing import List, Dict

# Assuming MEVStrategy is defined in a module named mev_strategy
from mev_strategy import MEVStrategy

class WalletSwarm:
    def __init__(self, mev_strategy, num_wallets: int, initial_balance: float):
        self.mev_strategy = mev_strategy
        self.num_wallets = num_wallets
        self.initial_balance = initial_balance
        self.wallets = []
        self.assets = {}

    def create_wallets(self):
        for i in range(self.num_wallets):
            wallet = self.mev_strategy.create_wallet()
            self.wallets.append(wallet)

    def allocate_assets(self):
        for wallet in self.wallets:
            assets = self.mev_strategy.allocate_assets(wallet, self.initial_balance)
            self.assets[wallet.address] = assets

    def calculate_total_net_value(self) -> float:
        total_net_value = 0
        for wallet in self.wallets:
            total_net_value += self.mev_strategy.calculate_net_value(wallet)
        return total_net_value

    def get_total_assets(self) -> List[str]:
        total_assets = []
        for assets in self.assets.values():
            total_assets.extend(assets)
        return list(set(total_assets))

    def get_asset_values(self) -> Dict[str, float]:
        asset_values = {}
        for wallet in self.wallets:
            assets = self.assets[wallet.address]
            for asset in assets:
                value = self.mev_strategy.get_asset_value(wallet, asset)
                if asset in asset_values:
                    asset_values[asset] += value
                else:
                    asset_values[asset] = value
        return asset_values

    def get_wallet_addresses(self) -> List[str]:
        return [wallet.address for wallet in self.wallets]

    def get_wallet_info(self, wallet_address: str) -> Dict[str, str]:
        wallet = next((w for w in self.wallets if w.address == wallet_address), None)
        if wallet:
            assets = self.assets[wallet_address]
            total_value = self.mev_strategy.calculate_net_value(wallet)
            asset_values = {asset: self.mev_strategy.get_asset_value(wallet, asset) for asset in assets}
            return {
                "address": wallet_address,
                "total_value": str(total_value),
                "assets": assets,
                "asset_values": asset_values
            }
        else:
            return {}

    def display_swarm_info(self):
        print("Total Net Value:", self.calculate_total_net_value())
        print("Total Assets:", self.get_total_assets())
        print("Asset Values:", self.get_asset_values())
        print("Wallet Addresses:", self.get_wallet_addresses())
        for wallet_address in self.get_wallet_addresses():
            wallet_info = self.get_wallet_info(wallet_address)
            print("Wallet", wallet_address, "Info:")
            print("Total Value:", wallet_info["total_value"])
            print("Assets:", wallet_info["assets"])
            print("Asset Values:", wallet_info["asset_values"])

if __name__ == "__main__":
    mev_strategy = MEVStrategy()  # Initialize MEV strategy
    num_wallets = 10
    initial_balance = 1000.0
    swarm = WalletSwarm(mev_strategy, num_wallets, initial_balance)
    swarm.create_wallets()
    swarm.allocate_assets()
    swarm.display_swarm_info()
