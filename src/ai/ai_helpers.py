# File: /src/ai/ai_helpers.py

class PredictionHelper:
    """
    Helper class for making and evaluating predictions in various AI models.
    """

    @staticmethod
    def evaluate_accuracy(predictions, actual):
        """
        Evaluate the accuracy of the model's predictions.
        
        :param predictions: The predicted values.
        :param actual: The actual observed values.
        :return: The accuracy as a percentage.
        """
        if len(predictions) != len(actual):
            raise ValueError("Predictions and actual values must have the same length.")
        
        correct = sum(1 for pred, act in zip(predictions, actual) if pred == act)
        return correct / len(predictions) * 100

    @staticmethod
    def normalize_data(data):
        """
        Normalize the input data to a range between 0 and 1.
        
        :param data: The data to normalize.
        :return: Normalized data.
        """
        min_val = min(data)
        max_val = max(data)
        return [(x - min_val) / (max_val - min_val) for x in data]


class ReinforcementLearningHelper:
    """
    Helper class for reinforcement learning techniques.
    """

    @staticmethod
    def compute_discounted_reward(rewards, gamma=0.99):
        """
        Compute the discounted reward for a series of rewards in reinforcement learning.
        
        :param rewards: A list of rewards over time.
        :param gamma: The discount factor for future rewards.
        :return: The discounted total reward.
        """
        discounted_reward = 0
        for t, reward in enumerate(rewards):
            discounted_reward += gamma ** t * reward
        
        return discounted_reward

    @staticmethod
    def choose_greedy_action(q_table, state, actions, exploration_rate=0.1):
        """
        Choose an action using an epsilon-greedy strategy.
        
        :param q_table: Q-Table that holds state-action values.
        :param state: The current state.
        :param actions: List of available actions.
        :param exploration_rate: The exploration rate (epsilon).
        :return: The chosen action.
        """
        import numpy as np
        if np.random.rand() < exploration_rate:
            return np.random.choice(actions)
        if state not in q_table:
            return np.random.choice(actions)
        
        return actions[np.argmax(q_table[state])]


class TokenSafetyHelper:
    """
    Helper class for checking the safety of tokens during transactions.
    """

    @staticmethod
    def is_token_safe(token_address):
        """
        Check if a given token is safe to interact with.
        
        :param token_address: The blockchain address of the token.
        :return: True if the token is safe, False otherwise.
        """
        # In a real system, this would check against a list of blacklisted tokens.
        return token_address not in ["0xScamToken1", "0xScamToken2"]

    @staticmethod
    def check_front_running_risk(gas_price, threshold=100):
        """
        Check if there is a front-running risk based on gas price.
        
        :param gas_price: The gas price for the transaction.
        :param threshold: The threshold for triggering a front-running alert.
        :return: True if there's a front-running risk, False otherwise.
        """
        return gas_price > threshold
