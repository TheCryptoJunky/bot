import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from ai.agents.q_learning_agent import QLearningAgent

class TestQLearningAgent(unittest.TestCase):

    def setUp(self):
        # Initialize the Q-learning agent
        self.agent = QLearningAgent()

    def test_update_q_table(self):
        """
        Test if the Q-table is correctly updated after taking an action and receiving a reward.
        """
        state = "state1"
        action = 0  # Assume 0 represents "buy"
        reward = 1
        next_state = "state2"

        # Perform the update
        self.agent.update_q_table(state, action, reward, next_state)

        # Check if the state is added to the Q-table
        self.assertIn(state, self.agent.q_table)

        # Check if the Q-value for the action was updated (should not be zero anymore)
        self.assertNotEqual(self.agent.q_table[state][action], 0)

if __name__ == '__main__':
    unittest.main()
