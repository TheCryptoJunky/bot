import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API keys for exchange access
    BINANCE_API_KEY = os.getenv('API_KEY_1')
    BINANCE_SECRET = os.getenv('SECRET_KEY_1')
    COINBASE_API_KEY = os.getenv('API_KEY_2')
    COINBASE_SECRET = os.getenv('SECRET_KEY_2')

    # AI model paths
    MODEL_PATH = os.getenv('MODEL_PATH')

    # Risk management settings
    MAX_DRAWDOWN = 0.2  # Maximum drawdown allowed (20%)
    MAX_POSITION_SIZE = 0.05  # Max position size per trade (5%)

    # Large order detection threshold for front-running
    LARGE_ORDER_THRESHOLD = 100  # Adjust based on market

    # Sentiment analysis API or data sources (optional)
    SENTIMENT_SOURCE_1 = os.getenv('SENTIMENT_SOURCE_1')
    SENTIMENT_SOURCE_2 = os.getenv('SENTIMENT_SOURCE_2')
