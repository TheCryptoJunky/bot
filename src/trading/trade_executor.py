# File: /src/trading/trade_executor.py
import logging
from datetime import datetime

class TradeExecutor:
    def __init__(self, db_connection):
        """
        Initializes the TradeExecutor with a given database connection.
        
        :param db_connection: Active MySQL connection instance.
        """
        self.db_connection = db_connection
        self.logger = logging.getLogger(__name__)

    def execute_trade(self, bot_name, trade_details):
        """
        Executes a trade and logs the results in the database.
        
        :param bot_name: The name of the bot executing the trade.
        :param trade_details: Dictionary containing trade details (symbol, amount, price).
        :return: None
        """
        try:
            # Example: Send the trade order to the exchange (to be implemented with ccxt or other libraries)
            self.logger.info(f"Executing trade for {bot_name}: {trade_details}")
            self.log_trade(bot_name, trade_details)
        except Exception as e:
            self.logger.error(f"Error executing trade for {bot_name}: {str(e)}")

    def log_trade(self, bot_name, trade_details):
        """
        Logs the trade details to the MySQL database.

        :param bot_name: The name of the bot that executed the trade.
        :param trade_details: Dictionary containing trade details (symbol, amount, price).
        :return: None
        """
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
            INSERT INTO trades (bot_name, symbol, amount, price, executed_at) 
            VALUES (%s, %s, %s, %s, %s)
            """, 
            (
                bot_name, 
                trade_details['symbol'], 
                trade_details['amount'], 
                trade_details['price'], 
                datetime.now()
            )
        )
        self.db_connection.commit()
