"""
Wallet class representing a digital wallet.

Attributes:
    balance (float): The current balance in the wallet.
    assets (dict): A dictionary of assets and their quantities.
"""

class Wallet:
    def __init__(self, balance=0.0, assets=None):
        """
        Initializes a Wallet object.

        Args:
            balance (float, optional): The initial balance. Defaults to 0.0.
            assets (dict, optional): A dictionary of assets and their quantities. Defaults to None.
        """
        self.balance = balance
        self.assets = assets if assets is not None else {}

    def get_balance(self):
        """
        Returns the current balance in the wallet.

        Returns:
            float: The current balance.
        """
        return self.balance

    def update_balance(self, amount):
        """
        Updates the balance in the wallet.

        Args:
            amount (float): The amount to add or subtract from the balance.
        """
        self.balance += amount

    def get_asset_quantity(self, asset):
        """
        Returns the quantity of a specific asset in the wallet.

        Args:
            asset (str): The asset to retrieve the quantity for.

        Returns:
            float: The quantity of the asset.
        """
        return self.assets.get(asset, 0.0)

    def update_asset_quantity(self, asset, quantity):
        """
        Updates the quantity of a specific asset in the wallet.

        Args:
            asset (str): The asset to update the quantity for.
            quantity (float): The new quantity of the asset.
        """
        self.assets[asset] = quantity

    def __str__(self):
        """
        Returns a string representation of the wallet.

        Returns:
            str: A string representation of the wallet.
        """
        return f"Wallet(balance={self.balance}, assets={self.assets})"
