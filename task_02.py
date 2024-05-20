def coincidence(data=None, sequence=None):
    if data is None or sequence is None:
        return []
    within_range = []

    for j in data:
        if isinstance(j, int) or isinstance(j, float):
            if sequence[0] <= j <= sequence[-1]:
                within_range.append(j)

    return within_range
