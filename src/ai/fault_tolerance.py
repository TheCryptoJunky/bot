import logging
import time
import random

class FaultTolerantAgent:
    """Fault-tolerant wrapper for RL agents with retry mechanisms and auto-restart."""

    def __init__(self, agent, max_retries=3, retry_delay=5):
        self.agent = agent
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def execute_with_retry(self, func, *args, **kwargs):
        """Execute a function with retry logic for fault tolerance."""
        retries = 0
        while retries < self.max_retries:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                retries += 1
                logging.error(f"Error occurred: {e}. Retrying {retries}/{self.max_retries}...")
                time.sleep(self.retry_delay)
        logging.error(f"Failed after {self.max_retries} retries.")
        raise Exception("Max retries exceeded")

    def restart_agent(self):
        """Simulate agent auto-restart in case of failure."""
        logging.info("Restarting agent...")
        time.sleep(random.uniform(1, 3))  # Simulate restart delay
        logging.info("Agent restarted successfully.")
