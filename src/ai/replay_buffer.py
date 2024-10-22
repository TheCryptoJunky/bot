import numpy as np
import random

class ExperienceReplayBuffer:
    """Experience Replay Buffer for storing and reusing experiences."""

    def __init__(self, capacity=10000):
        """Initialize the buffer with a fixed capacity."""
        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def push(self, state, action, reward, next_state, done):
        """Store a transition in the buffer."""
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (state, action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        """Sample a batch of experiences."""
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        """Return the current size of the buffer."""
        return len(self.buffer)

from .replay_buffer import ExperienceReplayBuffer
import numpy as np

class RLTradingAgent:
    """RL Trading Agent optimized with experience replay and batch processing."""

    def __init__(self, env, model_path=None, buffer_size=10000):
        """Initialize the RL agent with experience replay buffer."""
        self.env = env
        self.buffer = ExperienceReplayBuffer(buffer_size)
        self.model = PPO("MlpPolicy", self.env, verbose=1)

    def store_experience(self, state, action, reward, next_state, done):
        """Store experience in the replay buffer."""
        self.buffer.push(state, action, reward, next_state, done)

    def train_from_experience(self, batch_size=64):
        """Train the agent from a batch of experiences."""
        if len(self.buffer) >= batch_size:
            batch = self.buffer.sample(batch_size)
            states, actions, rewards, next_states, dones = zip(*batch)

            # Use batch processing to update the model
            for i in range(batch_size):
                self.model.learn(total_timesteps=1)
        else:
            logging.info("Not enough experiences in the buffer for training.")

import numpy as np
import logging

class RLTradingAgent:
    """RL Trading Agent with adaptive learning and fine-tuning."""

    def __init__(self, env, model_path=None):
        """Initialize the RL agent."""
        self.env = env
        self.model = PPO("MlpPolicy", self.env, verbose=1)
        
        if model_path:
            self.load_model(model_path)

    def fine_tune(self, new_data, fine_tune_steps=10000):
        """Fine-tune the agent based on new data."""
        self.env.envs[0].set_new_data(new_data)
        logging.info(f"Fine-tuning model with new data for {fine_tune_steps} steps.")
        self.model.learn(total_timesteps=fine_tune_steps)
        logging.info("Fine-tuning complete.")

    def adapt_to_market_changes(self, new_market_data, fine_tune_steps=5000):
        """Adapt agent strategies to new market conditions."""
        logging.info("Adapting to new market data...")
        self.fine_tune(new_market_data, fine_tune_steps=fine_tune_steps)
