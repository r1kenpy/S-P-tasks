def sort_list(array=None):
    if array is None:
        return []
    elif len(array) == 0:
        return array
    elif len(array) == 1:
        array.append(array[0])
        return array

    mi, ma = min(array), max(array)

    for i in range(len(array)):
        if array[i] == mi:
            array[i] = ma
        elif array[i] == ma:
            array[i] = mi
    array.append(mi)

    return array
