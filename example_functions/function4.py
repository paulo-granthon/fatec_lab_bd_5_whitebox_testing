def function4(n, depth=0):
    """
    Calculate the Fibonacci number recursively, but with added conditions:
    - If n is less than 0, return 'Invalid Input'.
    - If n is 0 or 1, return the base Fibonacci values.
    - If depth is greater than a threshold, stop the recursion.
    """
    if n < 0:
        return 'Invalid Input'
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 100 or depth > 100:
        return "Maximum Recursion Depth Reached"

    return function4(n-1, depth+1) + function4(n-2, depth+1)
