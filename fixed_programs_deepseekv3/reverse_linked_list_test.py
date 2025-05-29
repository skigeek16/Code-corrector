from .node import Node
from .reverse_linked_list import reverse_linked_list


def main():
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)

    result = reverse_linked_list(node5)

    if result == node1:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    while result:
        print(result.value, end=" ")
        result = result.successor
    print()
 
    node = Node(0)
    result = reverse_linked_list(node)

    if result == node:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    while result:
        print(result.value, end=" ")
        result = result.successor
    print()

    result = reverse_linked_list(None)
    if result == None:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    if result is not None:
        while result:
            print(result.value, end=" ")
            result = result.successor
    print()

if __name__ == "__main__":
    main()