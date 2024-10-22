# src/ai/arbitrage_strategy.py

class ArbitrageStrategy:
    """
    Implements an arbitrage strategy by comparing prices on a DEX and centralized exchange.
    """
    def __init__(self, dex_api, central_exchange_api):
        """
        Initialize the strategy with the given APIs.
        :param dex_api: API for the decentralized exchange.
        :param central_exchange_api: API for the centralized exchange.
        """
        self.dex_api = dex_api
        self.central_exchange_api = central_exchange_api

    def detect_arbitrage_opportunity(self, asset_id):
        """
        Detect arbitrage opportunities between exchanges.
        :param asset_id: The asset (e.g., BTC) to evaluate.
        """
        dex_price = self.dex_api.get_price(asset_id)
        central_price = self.central_exchange_api.get_price(asset_id)

        # Only execute trade if the price difference exceeds a threshold
        if central_price - dex_price > 10:
            self.dex_api.buy(asset_id, dex_price)
            self.central_exchange_api.sell(asset_id, central_price)
