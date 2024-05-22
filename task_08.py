def multiply_numbers(inputs=None):
    count = None

    if inputs is None:
        return None

    inputs = str(inputs)

    if inputs.isalpha():
        return None

    for element in inputs:
        if element.isdigit():
            element = int(element)
            if count is None:
                count = 1 * element
            else:
                count *= element
    return count
