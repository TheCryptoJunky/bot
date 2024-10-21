# File: /tests/test_reinforcement_learning_agent.py

import unittest
from src.ai.agents.reinforcement_learning_agent import RLTradingAgent  # Corrected import path

class TestRLTradingAgent(unittest.TestCase):
    """
    Unit test for the Reinforcement Learning (RL) Trading Agent. Verifies that the agent 
    can choose actions, learn from its environment, and update its decision-making process.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize RLTradingAgent for testing.
        """
        self.agent = RLTradingAgent()

    def test_choose_action(self):
        """
        Test that the agent chooses an action based on the state.
        """
        state = "price_up"
        action = self.agent.choose_action(state)
        self.assertIn(action, self.agent.actions)

    def test_q_table_update(self):
        """
        Test that the Q-table is updated correctly after taking an action.
        """
        state = "price_up"
        action = "buy"
        reward = 5
        next_state = "price_down"
        self.agent.update_q_table(state, action, reward, next_state)
        self.assertIn(state, self.agent.q_table)
        self.assertGreater(self.agent.q_table[state][self.agent.actions.index(action)], 0)

    def test_exploration_decay(self):
        """
        Test that the agent's exploration rate decays over time.
        """
        initial_rate = self.agent.exploration_rate
        self.agent.decay_exploration_rate()
        self.assertLess(self.agent.exploration_rate, initial_rate)

if __name__ == '__main__':
    unittest.main()
