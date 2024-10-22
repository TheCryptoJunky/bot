from kafka import KafkaConsumer
import json
import logging

class KafkaDataProcessor:
    """Process real-time market data using Kafka streams."""

    def __init__(self, topic, bootstrap_servers, trading_env):
        """Initialize the Kafka consumer to stream data into the trading environment."""
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='trading-bot-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.trading_env = trading_env

    def process_stream(self):
        """Continuously process the stream of market data and feed it into the trading environment."""
        for message in self.consumer:
            data = message.value
            logging.info(f"Received data: {data}")
            # Feed the data into the RL agent's environment for real-time decision making
            self.trading_env.update_market_data(data)
