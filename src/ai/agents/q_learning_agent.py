# File: /src/ai/agents/q_learning_agent.py

import numpy as np

class QLearningAgent:
    """
    Q-Learning Agent for training trading bots using reinforcement learning techniques.
    """

    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0):
        """
        Initialize the Q-Learning agent.
        
        :param actions: List of actions the agent can take (buy, sell, hold).
        :param learning_rate: Rate at which the agent learns from new experiences.
        :param discount_factor: Discount factor for future rewards.
        :param exploration_rate: Probability of exploring new actions vs exploiting known rewards.
        """
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = {}  # Dictionary storing state-action pairs

    def choose_action(self, state):
        """
        Choose an action based on the current state using epsilon-greedy strategy.
        
        :param state: The current state.
        :return: The selected action.
        """
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.actions)
        if state not in self.q_table:
            return np.random.choice(self.actions)
        return self.actions[np.argmax(self.q_table[state])]

    def update_q_table(self, state, action, reward, next_state):
        """
        Update the Q-table based on the action taken and reward received.
        
        :param state: The state before taking the action.
        :param action: The action taken.
        :param reward: The reward received for taking the action.
        :param next_state: The state resulting from the action.
        """
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        
        best_next_action = np.argmax(self.q_table.get(next_state, np.zeros(len(self.actions))))
        self.q_table[state][self.actions.index(action)] += self.learning_rate * (
            reward + self.discount
