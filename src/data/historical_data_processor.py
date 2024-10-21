import pandas as pd
import numpy as np

class HistoricalDataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        df = pd.read_csv(self.data_source)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        return df

    def preprocess_data(self, df):
        df = df[['Close']].values
        df_scaled = (df - np.mean(df)) / np.std(df)
        X, y = [], []
        for i in range(60, len(df_scaled)):
            X.append(df_scaled[i-60:i, 0])
            y.append(df_scaled[i, 0])
        return np.array(X), np.array(y)

    def prepare_training_data(self):
        df = self.load_data()
        X_train, y_train = self.preprocess_data(df)
        return X_train.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train
