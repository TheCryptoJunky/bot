import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class DatabaseConfig:
    """
    Configuration class for database-related settings.
    """
    HOST = os.getenv("MYSQL_HOST")
    USER = os.getenv("MYSQL_USER")
    PASSWORD = os.getenv("MYSQL_PASSWORD")
    DATABASE = os.getenv("MYSQL_DATABASE")


class LoggingConfig:
    """
    Configuration class for logging-related settings.
    """
    METHOD = os.getenv("LOGGING_METHOD", "file")  # Default to 'file' if not set
    DB_TABLE = os.getenv("LOG_DB_TABLE", "bot_logs")
    LEVEL = os.getenv("LOG_LEVEL", "INFO")  # Default to INFO


class TradeConfig:
    """
    Configuration class for trade execution-related settings.
    """
    API_KEY = os.getenv("TRADE_API_KEY")
    API_SECRET = os.getenv("TRADE_API_SECRET")


class BotConfig:
    """
    Configuration class for bot-specific settings.
    """
    BOT_NAME = os.getenv("BOT_NAME", "DefaultBot")
    MAX_TRADE_SIZE = int(os.getenv("MAX_TRADE_SIZE", 1000))
    MIN_TRADE_SIZE = int(os.getenv("MIN_TRADE_SIZE", 10))
    TRADE_TIMEOUT = int(os.getenv("TRADE_TIMEOUT", 30))  # in seconds


class SafetyConfig:
    """
    Configuration class for safety parameters and risk management.
    """
    CIRCUIT_BREAKER_THRESHOLD = int(os.getenv("CIRCUIT_BREAKER_THRESHOLD", 5000))
    REORG_CHECK_ENABLED = os.getenv("REORG_CHECK_ENABLED", "true").lower() == "true"
    POISON_TOKEN_CHECK_ENABLED = os.getenv("POISON_TOKEN_CHECK_ENABLED", "true").lower() == "true"


class AIConfig:
    """
    Configuration class for AI model-related settings.
    """
    MODEL_PATH = os.getenv("AI_MODEL_PATH", "models/trading_ai_model.h5")
    RETRAIN_INTERVAL = int(os.getenv("AI_RETRAIN_INTERVAL", 7))  # in days


class ListManagementConfig:
    """
    Configuration class for list management settings.
    """
    WHITELIST_AUTO_UPDATE = os.getenv("WHITELIST_AUTO_UPDATE", "false").lower() == "true"
    BLACKLIST_AUTO_UPDATE = os.getenv("BLACKLIST_AUTO_UPDATE", "true").lower() == "true"
    REDLIST_AUTO_UPDATE = os.getenv("REDLIST_AUTO_UPDATE", "true").lower() == "true"
    PUMPLIST_AUTO_MANAGEMENT = os.getenv("PUMPLIST_AUTO_MANAGEMENT", "true").lower() == "true"


class ExternalAPIConfig:
    """
    Configuration class for external API-related settings.
    """
    API_KEY = os.getenv("EXTERNAL_API_KEY")
    API_URL = os.getenv("EXTERNAL_API_URL", "https://api.external_service.com")


# Consolidating all configuration classes into one main class for ease of access
class Config:
    Database = DatabaseConfig
    Logging = LoggingConfig
    Trade = TradeConfig
    Bot = BotConfig
    Safety = SafetyConfig
    AI = AIConfig
    ListManagement = ListManagementConfig
    ExternalAPI = ExternalAPIConfig
