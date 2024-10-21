# File: /src/ai/agents/reinforcement_learning_agent.py

import numpy as np
import logging
from centralized_logger import CentralizedLogger
from src.ai.ai_helpers import RLHelper  # AI Helper for optimizing reinforcement learning strategies

# Initialize logger and centralized logging
logger = logging.getLogger(__name__)
centralized_logger = CentralizedLogger()

class RLTradingAgent:
    """
    A 5th-generation AI-driven reinforcement learning (RL) agent that dynamically adjusts trading strategies.
    The agent learns from real-time trading experiences, continuously refining its decision-making process
    using reinforcement learning techniques.
    """

    def __init__(self, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0, exploration_decay=0.995):
        """
        Initializes the RL agent with learning rate, discount factor, and exploration-exploitation parameters.
        The agent learns from real-time market experiences and optimizes future actions.
        """
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.q_table = {}  # Q-values for each state-action pair
        self.actions = ["buy", "sell", "hold"]  # Available actions
        self.rl_helper = RLHelper()  # AI Helper for advanced reinforcement learning

    def choose_action(self, state):
        """
        Chooses the best action based on the current state, balancing exploration vs. exploitation.
        AI Helper is used to optimize the decision-making process.
        """
        # Initialize state with zero Q-values if it's not in the Q-table
        if state not in self.q_table:
            self.q_table[state] = [0] * len(self.actions)

        # Exploration: Choose a random action
        if np.random.uniform(0, 1) < self.exploration_rate:
            action = np.random.choice(self.actions)
        else:
            # Exploitation: Choose the action with the highest Q-value
            action = self.rl_helper.optimize_action(self.q_table[state], self.actions)

        logger.info(f"Action chosen: {action} for state {state}")
        return action

    def update_q_table(self, state, action, reward, next_state):
        """
        Updates the Q-table based on the reward received and the next state.
        Uses AI-driven logic to optimize the learning process.
        """
        if state not in self.q_table:
            self.q_table[state] = [0] * len(self.actions)

        if next_state not in self.q_table:
            self.q_table[next_state] = [0] * len(self.actions)

        # Q-learning update formula
        action_index = self.actions.index(action)
        best_next_action = max(self.q_table[next_state])
        self.q_table[state][action_index] += self.learning_rate * (
            reward + self.discount_factor * best_next_action - self.q_table[state][action_index]
        )

        # Log the update to the Q-table
        centralized_logger.log_event(f"Q-table updated for state {state}, action {action}, reward {reward}")

    def decay_exploration_rate(self):
        """
        Decays the exploration rate over time, encouraging the agent to exploit learned strategies.
        """
        self.exploration_rate *= self.exploration_decay
        logger.info(f"Exploration rate decayed to {self.exploration_rate}")
