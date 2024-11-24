# calculator.py

class Calculator:
    def add(self, a, b):
        """Adds two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtracts second number from the first."""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers."""
        return a * b

    def divide(self, a, b):
        """Divides the first number by the second. Raises an error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
