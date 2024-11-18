import pytest
from example_functions import function2


@pytest.mark.parametrize("x, y, z, limit, operation, expected", [
    (1, 2, 3, 5, 'sum', 10),  # Sum of numbers from 1 to 4
    (1, 2, 3, 5, 'product', 24),  # Product of numbers from 1 to 4
    (1, 2, 3, 5, 'max', 3),  # Maximum value
    (1, 2, 3, 5, 'invalid', 'Invalid operation')  # Invalid operation
])
def test_function2(x, y, z, limit, operation, expected):
    """
    Test function2 for various operations (sum, product, max) and validate
    results.
    This ensures that different conditions and loops are covered.
    """
    result = function2(x, y, z, limit, operation)
    assert result == expected
