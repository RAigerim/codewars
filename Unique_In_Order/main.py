def unique_in_order(iterable):
    res = []
    if len(iterable) == 0: return []
    res.append(iterable[0])
    for i in range(1, len(iterable)):
        if iterable[i - 1] != iterable[i]:
            res.append(iterable[i])
    return res