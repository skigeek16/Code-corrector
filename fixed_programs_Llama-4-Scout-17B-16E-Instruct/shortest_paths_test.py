from .shortest_paths import shortest_paths


def main():
    graph = {
        ('A', 'B'): 1,
        ('A', 'C'): 3,
        ('B', 'C'): -2,
        ('B', 'D'): 4,
        ('C', 'D'): 7,
        ('C', 'E'): 4,
        ('D', 'E'): -5,
        ('E', 'F'): -1
    }
    result =  shortest_paths('A', graph)
    for path in result:
        print(path, result[path], end=" ")
    print()

    graph2 = {
        ('A', 'B'): 1,
        ('B', 'C'): 2,
        ('C', 'D'): 3,
        ('D', 'E'): -1,
        ('E', 'F'): 4
    }
    result =  shortest_paths('A', graph2)
    for path in result:
        print(path, result[path], end=" ")
    print()

    graph3 = {
        ('A', 'B'): 1,
        ('B', 'C'): 2,
        ('C', 'D'): 3,
        ('D', 'E'): -1,
        ('E', 'D'): 1,
        ('E', 'F'): 4,
        ('D', 'A'): -5
    }
    result =  shortest_paths('A', graph3)
    for path in result:
        print(path, result[path], end=" ")
    print()


if __name__ == "__main__":
    main()