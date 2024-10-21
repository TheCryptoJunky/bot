# File: /tests/test_circuit_breaker.py

import unittest
from src.safety.circuit_breaker import CircuitBreaker  # Corrected import path

class TestCircuitBreaker(unittest.TestCase):
    """
    Unit test for the CircuitBreaker class. Verifies that the circuit breaker
    correctly detects unsafe market conditions and halts operations.
    """

    def setUp(self):
        """
        Set up the test environment. Create an instance of the CircuitBreaker for testing.
        """
        self.circuit_breaker = CircuitBreaker(max_price_change=0.05, max_volume_spike=0.5)

    def test_initialization(self):
        """
        Test that the CircuitBreaker is initialized with the correct thresholds.
        """
        self.assertEqual(self.circuit_breaker.max_price_change, 0.05)
        self.assertEqual(self.circuit_breaker.max_volume_spike, 0.5)

    def test_check_status(self):
        """
        Test that the circuit breaker checks market conditions correctly.
        """
        self.circuit_breaker.is_triggered = True  # Simulate a triggered circuit breaker
        status = self.circuit_breaker.check_status()
        self.assertFalse(status)  # Circuit breaker should block operations

    def test_reset(self):
        """
        Test that the circuit breaker can be reset after being triggered.
        """
        self.circuit_breaker.is_triggered = True  # Simulate a triggered circuit breaker
        self.circuit_breaker.reset()
        self.assertFalse(self.circuit_breaker.is_triggered)

if __name__ == '__main__':
    unittest.main()
