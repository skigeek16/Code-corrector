def shortest_path_lengths(n, graph):
    distance = {i: float('inf') for i in range(n)}
    distance[0] = 0
    for _ in range(n-1):
        for u, v in graph:
            if distance[u] + v > distance[v]:
                distance[v] = distance[u] + v 
    for u, v in graph:
        if distance[u] + v > distance[v]:
            raise ValueError("Graph contains a negative weight cycle")
    return distance