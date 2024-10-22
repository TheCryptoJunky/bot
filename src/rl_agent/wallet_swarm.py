# wallet_swarm.py
import logging
import wallet

class WalletSwarm:
    def __init__(self, config):
        self.config = config
        self.wallets = []

    def add_wallet(self, wallet):
        self.wallets.append(wallet)

    def remove_wallet(self, wallet):
        self.wallets.remove(wallet)

    def get_wallets(self):
        return self.wallets

# Usage:
wallet_swarm = WalletSwarm(config)
wallet_swarm.add_wallet(wallet)
