def function2(x, y, z, limit, operation):
    """
    Loop through a range and perform different operations based on conditions.

    - If operation is 'sum', sum all values less than limit.
    - If operation is 'product', multiply all values less than limit.
    - If operation is 'max', return the maximum value among the parameters.
    """
    result = 0
    if operation == 'sum':
        for i in range(x, limit):
            result += i
        return result

    if operation == 'product':
        result = 1
        for i in range(x, limit):
            result *= i
        return result

    if operation == 'max':
        return max(x, y, z)

    return "Invalid operation"
