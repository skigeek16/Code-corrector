def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    def find(node):
        group = group_by_node.get(node)
        if group is None:
            group_by_node[node] = {node}
            return node
        if len(group) > 1:
            return next(iter(group))
        parent = next(iter(group))
        group_by_node[node] = group_by_node[parent]
        return find(parent)

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        u_root = find(u)
        v_root = find(v)
        if u_root != v_root:
            mst_edges.add(edge)
            group_by_node[u_root] = group_by_node.get(u_root, {u_root}).union(group_by_node.get(v_root, {v_root}))

    return mst_edges