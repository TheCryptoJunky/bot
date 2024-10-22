import numpy as np
import pandas as pd
from typing import Tuple

class QLearningAgent:
    def __init__(self, alpha: float, gamma: float, epsilon: float, num_states: int, num_actions: int):
        """
        Initialize Q-learning agent.

        Args:
        - alpha (float): Learning rate.
        - gamma (float): Discount factor.
        - epsilon (float): Exploration rate.
        - num_states (int): Number of states.
        - num_actions (int): Number of actions.
        """
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_states = num_states
        self.num_actions = num_actions
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state: int) -> int:
        """
        Choose an action using epsilon-greedy policy.

        Args:
        - state (int): Current state.

        Returns:
        - action (int): Chosen action.
        """
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state: int, action: int, reward: float, next_state: int) -> None:
        """
        Update Q-table using Q-learning update rule.

        Args:
        - state (int): Current state.
        - action (int): Chosen action.
        - reward (float): Received reward.
        - next_state (int): Next state.
        """
        q_value = self.q_table[state, action]
        next_q_value = self.q_table[next_state, np.argmax(self.q_table[next_state])]
        self.q_table[state, action] = (1 - self.alpha) * q_value + self.alpha * (reward + self.gamma * next_q_value)

    def save_q_table(self, file_path: str) -> None:
        """
        Save Q-table to a file.

        Args:
        - file_path (str): File path to save Q-table.
        """
        np.save(file_path, self.q_table)

    def load_q_table(self, file_path: str) -> None:
        """
        Load Q-table from a file.

        Args:
        - file_path (str): File path to load Q-table.
        """
        self.q_table = np.load(file_path)

def main():
    # Example usage
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.1, num_states=10, num_actions=3)
    state = 0
    action = agent.choose_action(state)
    reward = 10.0
    next_state = 1
    agent.update_q_table(state, action, reward, next_state)
    agent.save_q_table("q_table.npy")

if __name__ == "__main__":
    main()
