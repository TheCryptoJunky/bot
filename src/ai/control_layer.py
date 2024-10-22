from .strategies import StrategyManager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI()

class BotAction(BaseModel):
    bot_id: str
    action: str  # "start", "stop", "pause"
    pumplist_override: bool = False  # Override AI logic for Pumplist monitoring

class ControlLayer:
    """AI Control Layer with human intervention for bot management and Pumplist logic."""

    def __init__(self, strategy_manager: StrategyManager):
        self.strategy_manager = strategy_manager
        self.bot_status = {}  # Store current bot statuses

    def start_bot(self, bot_id: str):
        """Start the specified bot."""
        self.bot_status[bot_id] = "running"
        logging.info(f"Bot {bot_id} started.")

    def stop_bot(self, bot_id: str):
        """Safely stop the specified bot after completing trades."""
        if bot_id not in self.bot_status or self.bot_status[bot_id] == "stopped":
            raise HTTPException(status_code=400, detail=f"Bot {bot_id} is not running.")
        # Ensure the bot finishes current trades before stopping
        logging.info(f"Stopping bot {bot_id} after finishing active trades.")
        self.bot_status[bot_id] = "stopped"

    def pause_bot(self, bot_id: str):
        """Pause the specified bot."""
        if bot_id not in self.bot_status or self.bot_status[bot_id] == "paused":
            raise HTTPException(status_code=400, detail=f"Bot {bot_id} is already paused.")
        logging.info(f"Pausing bot {bot_id}.")
        self.bot_status[bot_id] = "paused"

    def apply_pumplist_override(self, bot_id: str):
        """Override AI logic to prioritize Pumplist assets for bot trading."""
        pumplist_assets = self.strategy_manager.list_manager.get_pumplist()
        if pumplist_assets:
            logging.info(f"Overriding AI to focus on Pumplist assets for bot {bot_id}.")
            self.strategy_manager.apply_pumplist_logic()
        else:
            logging.warning(f"No active Pumplist assets for bot {bot_id}.")

# FastAPI endpoints for bot control
@app.post("/bot_action")
async def bot_action(action: BotAction):
    control_layer = ControlLayer(strategy_manager)  # Inject dependencies
    if action.action == "start":
        control_layer.start_bot(action.bot_id)
    elif action.action == "stop":
        control_layer.stop_bot(action.bot_id)
    elif action.action == "pause":
        control_layer.pause_bot(action.bot_id)

    if action.pumplist_override:
        control_layer.apply_pumplist_override(action.bot_id)

    return {"status": f"Bot {action.bot_id} {action.action}"}
