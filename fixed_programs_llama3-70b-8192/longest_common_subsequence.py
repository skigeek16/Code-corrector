def longest_common_subsequence(a, b):
    if not a or not b:
        return ''
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b)
    else:
        seq1 = longest_common_subsequence(a, b[1:])
        seq2 = longest_common_subsequence(a[1:], b)
        return max(seq1, seq2, key=len)