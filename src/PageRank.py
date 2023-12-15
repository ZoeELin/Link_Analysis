def PageRank_iteration(graph, d):
    for node in graph.nodes:
        node.update_pagerank(d, len(graph.nodes))
    graph.normalize_pagerank()


def PageRank(graph, d, iteration):
    for i in range(iteration):
        PageRank_iteration(graph, d)
