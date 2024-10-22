from .rl_agent import RLTradingAgent
from .environment import TradingEnv

class MultiAgentManager:
    """Manages multiple trading agents using different strategies."""

    def __init__(self, agents_config, strategies):
        """Initialize the manager with agent configurations and strategies."""
        self.agents = []  # List to hold multiple trading agents
        for config in agents_config:
            # Create a trading environment and agent for each config
            env = TradingEnv(config['market_data'])
            agent = RLTradingAgent(env)
            self.agents.append(agent)

    def coordinate_agents(self):
        """Coordinate actions of all agents."""
        for agent in self.agents:
            reset_result = agent.env.reset()

            # Updated: Handle 2 or 3 values returned by reset()
            if isinstance(reset_result, tuple):
                if len(reset_result) == 2:
                    observation, _ = reset_result  # Unpack 2 values
                elif len(reset_result) == 3:
                    observation, _, _ = reset_result  # Unpack 3 values
            else:
                observation = reset_result  # Handle single value return

    def get_signals(self):
        """Get signals from all strategies."""
        return [agent.get_signal() for agent in self.agents]