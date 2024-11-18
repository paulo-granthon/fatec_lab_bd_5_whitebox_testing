import pytest
from example_functions import function4


@pytest.mark.parametrize("n, expected", [
    (-1, 'Invalid Input'),
    (0, 0),  # Base case
    (1, 1),  # Base case
    (5, 5),  # Recursive case
    (10, 55),  # Recursive case
    (1000, "Maximum Recursion Depth Reached"),  # Max depth
])
def test_function4(n, expected):
    """
    Test function4 for various values of n, covering base cases, recursive
    cases, and max recursion depth.
    This ensures that the recursion depth, base cases, and invalid inputs are
    correctly handled.
    """
    result = function4(n)
    assert result == expected
