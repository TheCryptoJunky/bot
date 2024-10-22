# src/ai/multi_strategy_manager.py

class MultiStrategyManager:
    """
    Manages multiple trading strategies and coordinates their execution.
    """
    def __init__(self, strategies):
        """
        Initialize the MultiStrategyManager with a list of strategies.
        :param strategies: List of strategy objects.
        """
        self.strategies = strategies

    def execute_all(self):
        """
        Execute all the strategies managed by this manager.
        """
        for strategy in self.strategies:
            strategy.execute()

    def get_signals(self):
        """
        Get trading signals from all strategies.
        :return: A dictionary of strategy names and their respective signals.
        """
        signals = {}
        for strategy in self.strategies:
            signals[strategy.__class__.__name__] = strategy.get_signal()
        return signals
