def HITS_iteration(graph):
    node_list = graph.nodes

    for node in node_list:
        node.update_authority()
    for node in node_list:
        node.update_hub()


def HITS(graph, iteration=10):
    for i in range(iteration):
        HITS_iteration(graph)
