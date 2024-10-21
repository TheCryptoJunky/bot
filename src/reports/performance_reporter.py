import pandas as pd
import matplotlib.pyplot as plt

class PerformanceReporter:
    def __init__(self, transaction_data):
        self.transaction_data = pd.DataFrame(transaction_data)

    def generate_summary(self):
        """Generates a performance summary of bots and strategies."""
        summary = self.transaction_data.groupby('bot_id').agg({
            'profit': 'sum',
            'trades': 'count',
            'win_rate': lambda x: (x > 0).mean()
        })
        return summary

    def plot_performance(self):
        """Plots the performance of the bots over time."""
        self.transaction_data['cumulative_profit'] = self.transaction_data['profit'].cumsum()
        self.transaction_data.plot(x='date', y='cumulative_profit', title='Cumulative Profit')
        plt.show()

    def compare_strategies(self):
        """Compares the performance of different strategies."""
        comparison = self.transaction_data.groupby('strategy').agg({
            'profit': 'sum',
            'win_rate': lambda x: (x > 0).mean()
        })
        return comparison
