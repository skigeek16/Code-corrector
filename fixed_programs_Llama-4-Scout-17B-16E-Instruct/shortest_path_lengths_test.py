from .shortest_path_lengths import shortest_path_lengths


def main():
    graph = {
        (0, 2): 3,
        (0, 5): 5,
        (2, 1): -2,
        (2, 3): 7,
        (2, 4): 4,
        (3, 4): -5,
        (4, 5): -1
    }
    result =  shortest_path_lengths(6, graph)
    for node_pairs in result:
        print(node_pairs, result[node_pairs], end=" ")
    print()

    graph2 = {
        (0, 1): 3,
        (1, 2): 5,
        (2, 3): -2,
        (3, 4): 7
    }
    result =  shortest_path_lengths(5, graph2)
    for node_pairs in result:
        print(node_pairs, result[node_pairs], end=" ")
    print()

    graph3 = {
        (0, 1): 3,
        (2, 3): 5
    }
    result =  shortest_path_lengths(4, graph3)
    for node_pairs in result:
        print(node_pairs, result[node_pairs], end=" ")
    print()

    graph4 = {
        (0, 1): 3,
        (1, 2): 5,
        (2, 0): -1
    }
    result =  shortest_path_lengths(3, graph4)
    for node_pairs in result:
        print(node_pairs, result[node_pairs], end=" ")
    print()


if __name__ == "__main__":
    main()