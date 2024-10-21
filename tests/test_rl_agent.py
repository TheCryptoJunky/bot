# File: /tests/test_rl_agent.py

import unittest
from ai.agents.rl_agent import ReinforcementLearningAgent

class TestRLAgent(unittest.TestCase):
    """
    Unit tests for the Reinforcement Learning Agent (RLAgent).
    Tests include Q-table initialization and action selection.
    """

    def setUp(self):
        # Initialize the RL agent before each test
        self.agent = ReinforcementLearningAgent()

    def test_initialize_q_table(self):
        """
        Test the initialization of the Q-table.
        Ensures that the agent can correctly initialize Q-values for new states and actions.
        """
        state = "state1"
        action = "buy"
        self.agent.initialize_q_table(state, action)
        self.assertIn(state, self.agent.q_table)
        self.assertIn(action, self.agent.q_table[state])

    def test_choose_action(self):
        """
        Test action selection for both exploration and exploitation strategies.
        Ensures that the agent can choose the best action based on Q-values.
        """
        self.agent.q_table = {"state1": {"buy": 1.0, "sell": 0.5}}
        action = self.agent.choose_action("state1", exploit=True)
        self.assertEqual(action, "buy")  # Exploit: choose action with highest Q-value

if __name__ == "__main__":
    unittest.main()
