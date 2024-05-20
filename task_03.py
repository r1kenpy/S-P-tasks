def max_odd(array):
    result = None
    for element in array:
        if isinstance(element, int) or isinstance(element, float):
            if element % 2 != 0 and (result is None or element > result):
                result = element

    return result
