import pytest
from example_functions import function5


@pytest.mark.parametrize("x, y, z, a, b, expected", [
    (5, -3, 4, 10, 10, 'Condition 1'),
    (1, 2, 3, 5, 5, 'Condition 2'),
    (1, 2, 3, 4, 5, 'Condition 3'),
])
def test_function5(x, y, z, a, b, expected):
    """
    Test function5 for different combinations of conditions to ensure all
    decision branches are covered.
    This validates logical flow and decision trees within the function.
    """
    result = function5(x, y, z, a, b)
    assert result == expected
