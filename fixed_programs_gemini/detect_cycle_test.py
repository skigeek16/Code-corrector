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
    node1_case2 = Node(1)
    node2_case2 = Node(2, node1_case2)
    node3_case2 = Node(3, node2_case2)
    node4_case2 = Node(4, node3_case2)
    node5_case2 = Node(5, node4_case2)
    node1_case2.successor = node5_case2

    if detect_cycle(node5_case2):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 3: 2-node list with cycle
    # Expected Output: Cycle detected!
    node1_case3 = Node(1)
    node2_case3 = Node(2, node1_case3)
    node1_case3.successor = node2_case3

    if detect_cycle(node2_case3):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()

    # Case 4: 2-node list with no cycle
    # Expected Output: Cycle not detected!
    node6 = Node(6)
    node7 = Node(7, node6)

    if detect_cycle(node7):
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
    node1_case6 = Node(1)
    node2_case6 = Node(2, node1_case6)
    node3_case6 = Node(3, node2_case6)
    node4_case6 = Node(4, node3_case6)
    node5_case6 = Node(5, node4_case6)
    node4_case6.successor = node5_case6
    node5_case6.successor = node4_case6

    if detect_cycle(node1_case6):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()


if __name__ == "__main__":
    main()