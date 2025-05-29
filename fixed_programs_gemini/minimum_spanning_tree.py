def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge

        group_u = group_by_node.get(u)
        if group_u is None:
            group_u = {u}
            group_by_node[u] = group_u

        group_v = group_by_node.get(v)
        if group_v is None:
            group_v = {v}
            group_by_node[v] = group_v

        if group_u != group_v:
            mst_edges.add(edge)
            union = group_u.union(group_v)
            for node in union:
                group_by_node[node] = union

    return mst_edges