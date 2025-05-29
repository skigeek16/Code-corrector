from collections import deque as Queue
 
def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while True:
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            successors = [node for node in node.successors if node not in nodesseen]
            queue.extend(successors)
            nodesseen.update(successors)

    return False