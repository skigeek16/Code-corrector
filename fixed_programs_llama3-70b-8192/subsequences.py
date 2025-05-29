def subsequences(a, b, k):
    if k == 0:
        return [[]]

    ret = []
    for i in range(a, b + 1 - k + 1):
        for rest in subsequences(i + 1, min(i + k, b), k - 1):
            ret.append([i] + rest)

    return ret