def lis(arr):
    ends = {0: 0}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends.get(length + 1, float('inf'))]:
            ends[length + 1] = i
            longest = length + 1

    return longest