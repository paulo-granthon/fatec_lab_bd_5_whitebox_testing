def function3(a, b, c, d, e):
    """
    This function checks several conditions:
    - If a is greater than b and c is less than d, return 'First Condition'.
    - If a + b == c * d, return 'Second Condition'.
    - If e is between 10 and 20, return 'Third Condition'.
    - If none of the above, return 'No Match'.
    """
    if a > b and c < d:
        return 'First Condition'

    if a + b == c * d:
        return 'Second Condition'

    if 10 <= e <= 20:
        return 'Third Condition'

    return 'No Match'
