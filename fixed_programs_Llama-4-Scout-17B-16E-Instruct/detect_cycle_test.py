from .node import Node
from .detect_cycle import detect_cycle

 
"""
Driver to test reverse linked list
"""
def main():
    # Case 1: 5-node list input with no cycle
    # Expected Output: Cycle not detected!
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)

    if detect_cycle(node5):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 2: 5-node list input with cycle
    # Expected Output: Cycle detected!
    node6 = Node(6)
    node7 = Node(7, node6)
    node8 = Node(8, node7)
    node9 = Node(9, node8)
    node10 = Node(10, node9)
    node10.successor = node7

    if detect_cycle(node10):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 3: 2-node list with cycle
    # Expected Output: Cycle detected!
    node11 = Node(11)
    node12 = Node(12, node11)
    node11.successor = node12

    if detect_cycle(node12):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 4: 2-node list with no cycle
    # Expected Output: Cycle not detected!
    node13 = Node(13)
    node14 = Node(14, node13)

    if detect_cycle(node14):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 5: 1-node list
    # Expected Output: Cycle not detected!
    node = Node(0)
    if detect_cycle(node):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 6: 5 nodes in total. the last 2 nodes form a cycle. input the first node
    node15 = Node(15)
    node16 = Node(16, node15)
    node15.successor = node16

    if detect_cycle(node15):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()


if __name__ == "__main__":
    main()