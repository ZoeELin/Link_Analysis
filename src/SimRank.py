def SimRank_iteration(graph, sim):
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            new_SimRank = sim.cal_SimRank(node1, node2)
            sim.update_sim_value(node1, node2, new_SimRank)

    sim.replace_sim()


def SimRank(graph, sim, iteration=100):
    for i in range(iteration):
        SimRank_iteration(graph, sim)
