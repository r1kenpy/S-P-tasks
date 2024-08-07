def connect_dicts(dict1: dict, dict2: dict):
    d1 = {}
    d2 = {}
    total = 0

    for key, value in dict1.items():
        if value >= 10:
            d1[key] = value
        total += value

    for key, value in dict2.items():
        if value >= 10:
            d2[key] = value
        total -= value

    return (
        dict(sorted({**d1, **d2}.items(), key=lambda items: items[1]))
        if total <= 0
        else dict(sorted({**d2, **d1}.items(), key=lambda items: items[1]))
    )
