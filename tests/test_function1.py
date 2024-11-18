import pytest
from example_functions import function1


@pytest.mark.parametrize("x, y, z, w, v, expected", [
    (-1, 2, 3, 4, 5, "Negative"),
    (2, 2, 2, 2, 2, "Even"),
    (1, 1, 1, 1, 1, "Odd"),
    (3, 3, 4, 5, 6, "Mixed"),
    (5, 3, 2, 6, 7, "Uncategorized"),
])
def test_function1(x, y, z, w, v, expected):
    """
    Test function1 for various combinations of even, odd, and negative numbers.
    This tests different combinations of conditions to ensure all branches are
    covered.
    """
    result = function1(x, y, z, w, v)
    assert result == expected
