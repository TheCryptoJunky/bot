# src/trading/trade_executor.py

class TradeExecutor:
    """
    Executes buy and sell trades based on the signals provided by trading strategies.
    """
    def __init__(self, trading_api):
        """
        Initialize the trade executor with a trading API.
        :param trading_api: An API object for executing trades on exchanges.
        """
        self.trading_api = trading_api

    def execute_trade(self, asset, action, amount):
        """
        Execute a trade based on the given action.
        :param asset: The asset to trade (e.g., 'BTC').
        :param action: 'buy' or 'sell'.
        :param amount: Amount of the asset to trade.
        :return: The result of the trade execution.
        """
        if action == 'buy':
            return self.trading_api.buy(asset, amount)
        elif action == 'sell':
            return self.trading_api.sell(asset, amount)
        else:
            raise ValueError(f"Unknown action: {action}")
