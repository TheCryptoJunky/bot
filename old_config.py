# /config.py

import os

class ConfigError(Exception):
    """Custom exception for configuration errors.
    Raised when mandatory environment variables are missing or misconfigured.
    """
    pass

class Config:
    """Centralized configuration loaded from environment variables."""

    def __init__(self):
        # Ensure all critical environment variables are set
        self.check_mandatory_vars()

    @staticmethod
    def check_mandatory_vars():
        """
        Ensures that all required environment variables are present.
        Raises ConfigError if any mandatory variables are missing.
        """
        mandatory_vars = [
            'API_KEY_1', 'SECRET_KEY_1', 'MYSQL_HOST', 
            'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DATABASE'
        ]
        for var in mandatory_vars:
            if not os.getenv(var):
                raise ConfigError(f"Mandatory environment variable {var} is missing.")

    # API Keys for multiple exchanges
    API_KEYS = {
        'BINANCE': {
            'API_KEY': os.getenv('API_KEY_1'),   # Binance API Key
            'SECRET': os.getenv('SECRET_KEY_1')  # Binance Secret Key
        },
        'COINBASE': {
            'API_KEY': os.getenv('API_KEY_2'),   # Coinbase API Key
            'SECRET': os.getenv('SECRET_KEY_2')  # Coinbase Secret Key
        },
        'UNISWAP': {
            'API_KEY': os.getenv('API_KEY_3'),   # Uniswap API Key
            'SECRET': os.getenv('SECRET_KEY_3')  # Uniswap Secret Key
        }
    }

    # Risk management settings (using environment variables with defaults)
    RISK_MANAGEMENT = {
        'MAX_DRAWDOWN': float(os.getenv('MAX_DRAWDOWN', 0.2)),  # Default max drawdown: 20%
        'MAX_POSITION_SIZE': float(os.getenv('MAX_POSITION_SIZE', 0.05))  # Default max position size: 5%
    }

    # Sentiment analysis sources (dynamically loaded via environment)
    SENTIMENT_SOURCES = {
        'NEWS': os.getenv('SENTIMENT_SOURCE_1', 'default-news-source'),
        'SOCIAL_MEDIA': os.getenv('SENTIMENT_SOURCE_2', 'default-social-source')
    }

    # Telegram configuration
    TELEGRAM = {
        'BOT_TOKEN': os.getenv('TELEGRAM_BOT_TOKEN'),
        'CHAT_ID': os.getenv('TELEGRAM_CHAT_ID')
    }

    # Twilio configuration
    TWILIO = {
        'ACCOUNT_SID': os.getenv('TWILIO_ACCOUNT_SID'),
        'AUTH_TOKEN': os.getenv('TWILIO_AUTH_TOKEN'),
        'FROM_NUMBER': os.getenv('TWILIO_FROM_NUMBER'),
        'TO_NUMBER': os.getenv('TWILIO_TO_NUMBER')
    }

    # Error handling configuration
    ERROR_HANDLING = {
        'ERROR_THRESHOLD': int(os.getenv('ERROR_THRESHOLD', '5')),  # Max allowed errors (default 5)
        'RETRY_ATTEMPTS': int(os.getenv('RETRY_ATTEMPTS', '3'))  # Retry attempts on failure
    }

    # Trading configuration
    TRADING = {
        'FEE_RATE': float(os.getenv('FEE_RATE', '0.001')),  # Trading fee rate (default 0.1%)
        'TRADE_SYMBOLS': os.getenv('TRADE_SYMBOLS', 'BTC/USDT,ETH/USDT').split(',')  # Default trade pairs
    }

    # AI model paths (can be loaded dynamically via env variables)
    MODEL_PATH = os.getenv('MODEL_PATH', 'default/model/path')

    # MySQL database configuration
    DB = {
        'HOST': os.getenv('MYSQL_HOST'),
        'USER': os.getenv('MYSQL_USER'),
        'PASS': os.getenv('MYSQL_PASSWORD'),
        'NAME': os.getenv('MYSQL_DATABASE')
    }

    # External data sources (e.g., mempool)
    MEMPOOL = {
        'API_URL': "https://api.mempool.com",  # Mempool API URL
        'API_KEY': os.getenv('MEMPOOL_API_KEY', 'default-mempool-key')
    }
