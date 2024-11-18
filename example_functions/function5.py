def function5(x, y, z, a, b):
    """
    Evaluate several conditions based on input values:
    - If x is positive, y is negative, and z is even, return 'Condition 1'.
    - If a equals b and x and y are greater than 0, return 'Condition 2'.
    - If none of the above, return 'Condition 3'.
    """
    if y < 0 < x and z % 2 == 0:
        return 'Condition 1'

    if a == b and x > 0 and y > 0:
        return 'Condition 2'

    return 'Condition 3'
