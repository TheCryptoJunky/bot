# File: /tests/test_q_learning_agent.py

import unittest
from src.ai.agents.q_learning_agent import QLearningAgent  # Corrected import path

class TestQLearningAgent(unittest.TestCase):
    """
    Unit test for the Q-Learning Agent. Verifies that the agent correctly
    learns from its environment and updates the Q-table.
    """

    def setUp(self):
        """
        Set up the test environment. Initialize QLearningAgent for testing.
        """
        self.agent = QLearningAgent(actions=['buy', 'sell', 'hold'])

    def test_choose_action(self):
        """
        Test that the agent correctly chooses an action based on the state.
        """
        state = 'price_up'
        action = self.agent.choose_action(state)
        self.assertIn(action, ['buy', 'sell', 'hold'])

    def test_q_table_update(self):
        """
        Test that the Q-table is updated correctly after an action is taken.
        """
        state = 'price_up'
        next_state = 'price_down'
        action = 'buy'
        reward = 10
        self.agent.update_q_table(state, action, reward, next_state)
        self.assertIn(state, self.agent.q_table)
        self.assertGreater(self.agent.q_table[state][self.agent.actions.index(action)], 0)

    def test_exploration_decay(self):
        """
        Test that the exploration rate decays over time.
        """
        initial_exploration_rate = self.agent.exploration_rate
        self.agent.decay_exploration_rate()
        self.assertLess(self.agent.exploration_rate, initial_exploration_rate)

if __name__ == '__main__':
    unittest.main()
