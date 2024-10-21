import ccxt
import pandas as pd
import numpy as np

class RealTimeDataCollector:
    def __init__(self, exchange_name='binance'):
        self.exchange = getattr(ccxt, exchange_name)()

    def fetch_real_time_data(self, symbol='BTC/USDT'):
        ticker = self.exchange.fetch_ticker(symbol)
        df = pd.DataFrame([ticker])
        df['Date'] = pd.to_datetime('now')
        return df[['Date', 'close']].rename(columns={'close': 'Close'})

    def preprocess_real_time_data(self, df):
        df_scaled = (df['Close'] - np.mean(df['Close'])) / np.std(df['Close'])
        X = df_scaled.values.reshape((1, 60, 1))
        return X
