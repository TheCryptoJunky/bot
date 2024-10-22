import websocket
import json
import logging

class RealTimeDataCollector:
    """Collect real-time market data and provide it to RL agents."""

    def __init__(self, ws_url, trading_env):
        self.ws_url = ws_url
        self.trading_env = trading_env  # Reference to RL agent's environment

    def on_message(self, ws, message):
        """Process incoming real-time data."""
        data = json.loads(message)
        logging.info(f"Received market data: {data}")

        # Feed the data into the trading environment
        self.trading_env.update_market_data(data)

    def on_error(self, ws, error):
        """Handle any errors that occur."""
        logging.error(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        """Handle the WebSocket closure."""
        logging.info(f"WebSocket closed: {close_msg}")

    def on_open(self, ws):
        """Called when the WebSocket connection is established."""
        logging.info("WebSocket connection opened.")

    def start_stream(self):
        """Start the WebSocket stream to collect real-time data."""
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self.ws_url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()
