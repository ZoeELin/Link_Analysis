def PageRank_iteration(graph, d):
    node_list_origin = graph.nodes
    # pageranks = {node.name: 1 / len(graph.nodes) for node in graph.nodes}
    new_node = {}
    for node in node_list_origin:
        new_pagerank = node.cal_pagerank(d, len(graph.nodes))
        new_node[node.name] = new_pagerank

    for node in node_list_origin:
        node.pagerank = new_node[node.name]

    graph.normalize_pagerank()


def PageRank(graph, d, iteration):
    for i in range(iteration):
        PageRank_iteration(graph, d)
