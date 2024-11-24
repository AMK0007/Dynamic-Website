import math


# Calculator Application Code
class Calculator:
    def add(self, a, b):
        """Adds two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtracts two numbers"""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers"""
        return a * b

    def divide(self, a, b):
        """Divides two numbers. Handles division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sqrt(self, a):
        """Returns the square root of a number."""
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)


# Pytest Tests for the Calculator App
import pytest

@pytest.fixture
def calculator():
    """Fixture to initialize the calculator before each test."""
    return Calculator()

def test_add(calculator):
    """Test for the add method"""
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    """Test for the subtract method"""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(2, 2) == 0
    assert calculator.subtract(0, 5) == -5

def test_multiply(calculator):
    """Test for the multiply method"""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 10) == 0

def test_divide(calculator):
    """Test for the divide method"""
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(10, 2) == 5
    
    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)

def test_sqrt(calculator):
    """Test for the sqrt method"""
    assert calculator.sqrt(9) == 3
    assert calculator.sqrt(16) == 4
    
    # Test square root of negative number
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        calculator.sqrt(-4)

# If this script is executed directly, the tests will be run.
if __name__ == "__main__":
    pytest.main()
