def shortest_path_lengths(num_vertices, graph):
    """
    Calculates shortest path lengths between all pairs of vertices in a graph using the Bellman-Ford algorithm.

    Args:
        num_vertices (int): The number of vertices in the graph. Vertices are assumed to be numbered from 0 to num_vertices - 1.
        graph (dict): A dictionary representing the graph where keys are tuples (u, v) representing an edge from u to v, and values are the edge weights.

    Returns:
        dict: A dictionary where keys are tuples (u, v) representing a pair of vertices, and values are the shortest path lengths from u to v.
              If there is no path from u to v, the value is float('inf').
              If there is a negative cycle reachable from u, the value is float('-inf').
    """

    dist = {}
    for u in range(num_vertices):
        for v in range(num_vertices):
            dist[(u, v)] = float('inf')
        dist[(u, u)] = 0

    for _ in range(num_vertices - 1):
        for (u, v), weight in graph.items():
            if dist[(u, u)] != float('-inf') and dist[(u, v)] != float('-inf') and dist[(u, v)] > dist[(u, u)] + weight:
                dist[(u, v)] = dist[(u, u)] + weight
                
    for _ in range(num_vertices):
        for (u, v), weight in graph.items():
             if dist[(u, u)] != float('-inf') and dist[(u, v)] != float('-inf') and dist[(u, v)] > dist[(u, u)] + weight:
                dist[(u, v)] = float('-inf')

    return dist