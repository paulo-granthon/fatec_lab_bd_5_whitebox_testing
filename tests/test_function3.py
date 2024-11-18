import pytest
from example_functions import function3


@pytest.mark.parametrize("a, b, c, d, e, expected", [
    (5, 3, 2, 4, 15, 'First Condition'),
    (9, 9, 3, 6, 0, 'Second Condition'),
    (3, 3, 3, 3, 15, 'Third Condition'),
    (1, 2, 3, 4, 25, 'No Match'),
])
def test_function3(a, b, c, d, e, expected):
    """
    Test function3 for various combinations of conditions to ensure all paths
    are covered.
    This validates decision branches and ensures proper logical flow.
    """
    result = function3(a, b, c, d, e)
    assert result == expected
