import copy


class Similarity:
    def __init__(self, graph, decay_factor):
        self.decay_factor = decay_factor
        self.name_list, self.old_sim = self.init_sim(graph)
        self.node_num = len(self.name_list)
        self.new_sim = [[0] * self.node_num for i in range(self.node_num)]

    def init_sim(self, graph):
        name_list = [node.name for node in graph.nodes]
        sim = []
        for name1 in name_list:
            temp_sim = []
            for name2 in name_list:
                if name1 == name2:
                    temp_sim.append(1)
                else:
                    temp_sim.append(0)
            sim.append(temp_sim)
        return name_list, sim

    def get_name_index(self, name):
        return self.name_list.index(name)

    def get_sim_value(self, node1, node2):
        node1_idx = self.get_name_index(node1.name)
        node2_idx = self.get_name_index(node2.name)
        return self.old_sim[node1_idx][node2_idx]

    def cal_SimRank(self, node1, node2):
        if node1.name == node2.name:
            return 1

        if len(node1.parents) == 0 or len(node2.parents) == 0:
            return 0

        sum_SimRank = 0
        for neighbor1 in node1.parents:
            for neighbor2 in node2.parents:
                sum_SimRank += self.get_sim_value(neighbor1, neighbor2)

        scale = self.decay_factor / (len(node1.parents) * len(node2.parents))
        new_SimRank = scale * sum_SimRank

        return new_SimRank

    def update_sim_value(self, node1, node2, value):
        node1_idx = self.get_name_index(node1.name)
        node2_idx = self.get_name_index(node2.name)
        self.new_sim[node1_idx][node2_idx] = value

    def replace_sim(self):
        self.old_sim = copy.deepcopy(self.new_sim)
