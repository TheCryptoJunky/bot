# src/ai/momentum_strategy.py

class MomentumStrategy:
    """
    Implements a momentum-based trading strategy.
    """
    def __init__(self, trading_env):
        """
        Initialize the strategy with the given trading environment.
        :param trading_env: The environment that provides price and momentum data.
        """
        self.trading_env = trading_env

    def get_signal(self):
        """
        Generate buy/sell signals based on the momentum.
        :return: 'buy', 'sell', or 'hold' based on the momentum value.
        """
        momentum = self.trading_env.get_momentum()

        if momentum > 0:
            return "buy"
        elif momentum < 0:
            return "sell"
        else:
            return "hold"

    def execute_trade(self):
        """
        Execute a trade based on the momentum signal.
        """
        signal = self.get_signal()
        if signal == "buy":
            self.trading_env.buy()
        elif signal == "sell":
            self.trading_env.sell()
