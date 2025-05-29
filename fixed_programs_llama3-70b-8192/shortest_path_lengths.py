from collections import defaultdict

def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update((i,j,v) for (i,j),v in length_by_edge.items())
 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    length_by_path[i, k] + length_by_path[k, j]
                )

    return length_by_path