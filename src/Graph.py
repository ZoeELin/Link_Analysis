class Graph:
    def __init__(self):
        self.nodes = []

    # 找到需要的節點，如果沒有就建立 new_node
    # return node (not node name)
    def find(self, name):
        # Graph 中沒有這個 node，就把他加進 graph 之中
        find_node = next((node for node in self.nodes if node.name == name), None)
        if not find_node:
            new_node = Node(name)
            self.nodes.append(new_node)
            return new_node
        return find_node

    # 建立 Graph 時使用
    # 把這個 node 的 parent, child 前後連上
    def add_edge(self, parent, child):
        parent_node = self.find(parent)
        child_node = self.find(child)

        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    # 建立 Graph 時使用
    # 排列節點（方便整理）
    def sort_nodes(self):
        self.nodes.sort(key=lambda node: int(node.name))

    def display(self):
        for node in self.nodes:
            print(f"{node.name} -> {[child.name for child in node.children]}")

    def get_auth_hub_list(self):
        authority_list = []
        hub_list = []
        for node in self.nodes:
            authority_list.append(node.authority)
            hub_list.append(node.hub)

        return authority_list, hub_list

    def normalize_authority_hub(self):
        authority_sum = sum(node.authority for node in self.nodes)
        hub_sum = sum(node.hub for node in self.nodes)

        for node in self.nodes:
            node.authority = node.authority / authority_sum
            node.hub = node.hub / hub_sum

    def get_pagerank_list(self):
        pagerank_list = [node.pagerank for node in self.nodes]

        return pagerank_list

    def normalize_pagerank(self):
        pagerank_sum = sum([node.pagerank for node in self.nodes])
        for node in self.nodes:
            node.pagerank = node.pagerank / pagerank_sum


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.authority = 1
        self.hub = 1
        self.pagerank = 1

    def link_child(self, new_child):
        if new_child in self.children:
            return None
        self.children.append(new_child)

    def link_parent(self, new_parent):
        if new_parent in self.parents:
            return None
        self.parents.append(new_parent)

    def update_authority(self):
        self.authority = sum(node.hub for node in self.parents)

    def update_hub(self):
        self.hub = sum(node.authority for node in self.children)

    def update_pagerank(self, d, n):
        in_neighbors = self.parents
        pagerank_sum = sum(
            (node.pagerank / len(node.children)) for node in in_neighbors
        )
        random_jumping = d / n
        self.pagerank = random_jumping + (1 - d) * pagerank_sum
