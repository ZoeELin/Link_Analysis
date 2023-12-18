def HITS_iteration(graph):
    node_list_origin = graph.nodes
    new_values = {}

    for node in node_list_origin:
        new_authority = node.cal_authority()
        new_hub = node.cal_hub()
        new_values[node.name] = (new_authority, new_hub)

    for node in node_list_origin:
        node.authority, node.hub = new_values[node.name]

    graph.normalize_authority_hub()


def HITS(graph, iteration=10):
    for i in range(iteration):
        HITS_iteration(graph)
