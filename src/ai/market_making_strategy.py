import logging

class MarketMakingStrategy:
    """Market-making strategy to provide liquidity and profit from bid-ask spreads."""

    def __init__(self, trading_env, spread=0.02):
        """Initialize the market-making strategy with a predefined spread."""
        self.env = trading_env
        self.spread = spread

    def place_orders(self, asset_id, mid_price):
        """Place both buy and sell orders around the mid-price to provide liquidity."""
        buy_price = mid_price * (1 - self.spread / 2)
        sell_price = mid_price * (1 + self.spread / 2)

        logging.info(f"Placing buy order for {asset_id} at {buy_price} and sell order at {sell_price}")
        self.env.place_buy_order(asset_id, buy_price)
        self.env.place_sell_order(asset_id, sell_price)

    def execute_market_making(self, asset_id, mid_price):
        """Execute the market-making strategy."""
        self.place_orders(asset_id, mid_price)
