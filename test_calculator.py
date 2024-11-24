# test_calculator.py

import pytest
from calculator import Calculator  # Import the Calculator class from the calculator.py file

@pytest.fixture
def calculator():
    """Fixture to create a Calculator object."""
    return Calculator()

def test_add(calculator):
    """Test for the add method of Calculator."""
    assert calculator.add(1, 2) == 3

def test_subtract(calculator):
    """Test for the subtract method of Calculator."""
    assert calculator.subtract(5, 3) == 2

def test_multiply(calculator):
    """Test for the multiply method of Calculator."""
    assert calculator.multiply(3, 4) == 12

def test_divide(calculator):
    """Test for the divide method of Calculator."""
    assert calculator.divide(6, 3) == 2
    
    # Test division by zero which should raise a ValueError
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
