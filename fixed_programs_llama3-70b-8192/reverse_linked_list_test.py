node1 = Node(1)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)
node5 = Node(5, None)
node1.successor = node2.successor = node1
node3.successor = node2
node4.successor = node3