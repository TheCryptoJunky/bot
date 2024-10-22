import torch
import torch.nn as nn

class DNNTradingModel(nn.Module):
    """Deep Neural Network model for processing trading data."""

    def __init__(self, input_size, hidden_size, output_size):
        """Initialize the DNN model."""
        super(DNNTradingModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        """Forward pass through the DNN."""
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x
