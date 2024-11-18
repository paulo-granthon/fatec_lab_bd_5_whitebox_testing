def function1(x, y, z, w, v):
    """
    Perform multiple checks to return a string based on the parameters.

    Checks:
    1. If any number is negative, returns 'Negative'.
    2. If all numbers are even, returns 'Even'.
    3. If all numbers are odd, returns 'Odd'.
    4. If x + y is even and z + w is odd, returns 'Mixed'.
    5. If any other combination, returns 'Uncategorized'.
    """
    if x < 0 or y < 0 or z < 0 or w < 0 or v < 0:
        return 'Negative'

    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and w % 2 == 0 and v % 2 == 0:
        return 'Even'

    if x % 2 != 0 and y % 2 != 0 and z % 2 != 0 and w % 2 != 0 and v % 2 != 0:
        return 'Odd'

    if (x + y) % 2 == 0 and (z + w) % 2 != 0:
        return 'Mixed'

    return 'Uncategorized'
