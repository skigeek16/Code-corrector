class Node:
    def __init__(self, value=None, successor_node=None, successor_nodes=None, predecessor_nodes=None, incoming_nodes=None, outgoing_nodes=None):
        self.value = value
        self.successor_node = successor_node
        self.successor_nodes = successor_nodes if successor_nodes is not None else []
        self.predecessor_nodes = predecessor_nodes if predecessor_nodes is not None else []
        self.incoming_nodes = incoming_nodes if incoming_nodes is not None else []
        self.outgoing_nodes = outgoing_nodes if outgoing_nodes is not None else []

    def get_successor(self):
        return self.successor_node

    def get_successors(self):
        return self.successor_nodes

    def get_predecessors(self):
        return self.predecessor_nodes