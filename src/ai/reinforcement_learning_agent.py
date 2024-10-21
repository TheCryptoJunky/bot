# /src/ai/reinforcement_learning_agent.py

from stable_baselines3 import PPO  # Reinforcement learning algorithm
import numpy as np

class RLTradingAgent:
    """
    Reinforcement Learning Trading Agent using PPO.
    Combines inputs from various AI models and adjusts strategies dynamically based on performance.
    """

    def __init__(self, environment, feature_inputs):
        self.env = environment
        self.model = PPO("MlpPolicy", self.env, verbose=1)
        self.feature_inputs = feature_inputs  # Input from supporting models (LSTM, Sentiment, ARIMA, etc.)
        
        # Initialize weight distribution for AI models
        self.current_weights = {
            "lstm": 0.3,
            "sentiment": 0.2,
            "arima": 0.2,
            "technical": 0.2,
            "market_regime": 0.1
        }

    def adjust_weights(self, performance_metrics):
        """
        Adjusts the weights of various inputs based on their performance.
        Increases the weight for models with positive performance and decreases for poor-performing models.
        """
        for module, performance in performance_metrics.items():
            self.current_weights[module] += 0.1 if performance > 0 else -0.1
            self.current_weights[module] = max(min(self.current_weights[module], 1), 0)

    def get_weighted_input(self, observations):
        """
        Combines input from various models into a single weighted input.
        Each model's input is multiplied by its respective weight to create a final input value.
        """
        weighted_input = 0
        for module, input_value in observations.items():
            weighted_input += self.current_weights[module] * input_value
        return weighted_input

    def train_agent(self, total_timesteps=10000):
        """
        Trains the agent using the PPO algorithm on historical data for a specified number of timesteps.
        """
        self.model.learn(total_timesteps=total_timesteps)

    def get_action(self, observation):
        """
        Returns an action based on the current weighted input from multiple models.
        The action is determined using the PPO algorithm.
        """
        weighted_input = self.get_weighted_input(observation)
        return self.model.predict(weighted_input, deterministic=True)[0]

    def rebalance_phase(self):
        """
        Switches the strategy weights during a rebalancing phase, giving more weight to certain models like ARIMA.
        This happens when liquidity is high or market conditions require a more conservative approach.
        """
        self.current_weights = {
            "lstm": 0.1,
            "sentiment": 0.1,
            "arima": 0.4,
            "technical": 0.1,
            "market_regime": 0.3
        }
