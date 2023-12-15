import numpy as np
import os

from src.Graph import Graph
from src.Similarity import Similarity
from src.HITS import HITS
from src.PageRank import PageRank
from src.SimRank import SimRank


# 初始化 graph，
# 包括讀 .txt 檔與建立 Graph
def init_graph(fname):
    # 讀.txt檔
    with open(fname) as f:
        lines = f.readlines()

    # 定義 graph = Graph()
    graph = Graph()

    # 建立成 graph
    for line in lines:
        [parent, child] = line.strip().split(",")
        graph.add_edge(parent, child)

    graph.sort_nodes()

    return graph


def output_HITS(iteration, graph, result_dir, fname):
    # 定義保存權威分數和中心分數的文件名
    authority_fname = "_HITS_authority.txt"
    hub_fname = "_HITS_hub.txt"

    # 執行HITS算法
    HITS(graph, iteration)  # 執行HITS算法，傳入圖和迭代次數

    graph.normalize_authority_hub()

    # 從圖中獲取計算後的 authority score 和 hub score
    authority_list, hub_list = graph.get_auth_hub_list()

    # Authority score
    print()
    print("Authority:")
    print(authority_list)
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    # 將 authority score 儲存到文件
    np.savetxt(
        os.path.join(path, fname + authority_fname),
        np.asarray(authority_list, dtype="float32"),
        fmt="%.3f",
        newline=" ",
    )

    # Hub score
    print("Hub:")
    print(hub_list)  # 輸出 hub score
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)

    # 將 hub score 保存到文件
    np.savetxt(
        os.path.join(path, fname + hub_fname),
        np.asarray(hub_list, dtype="float32"),
        fmt="%.3f",
        newline=" ",
    )


def output_PageRank(iteration, graph, damping_factor, result_dir, fname):
    pagerank_fname = "_PageRank.txt"
    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()

    # PageRank score
    print("PageRank:")
    print(pagerank_list)  # 輸出 pagerank score
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)

    np.savetxt(
        os.path.join(path, fname + pagerank_fname),
        np.asarray(pagerank_list, dtype="float32"),
        fmt="%.3f",
        newline=" ",
    )


def output_SimRank(iteration, graph, decay_factor, result_dir, fname):
    simrank_fname = "_SimRank.txt"

    sim = Similarity(graph, decay_factor)

    SimRank(graph, sim, iteration)
    ans_metrix = sim.new_sim
    print()
    print("SimRank:")
    print(ans_metrix)
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)

    np.savetxt(
        os.path.join(path, fname + simrank_fname),
        np.asarray(ans_metrix, dtype="float32"),
        fmt="%.3f",
        newline=" ",
    )


# python main.py --input_file 'dataset/graph_1.txt' --damping_factor 0.15 --decay_factor 0.9 --iteration 500
if __name__ == "__main__":
    file_path = "dataset/graph_4.txt"
    damping_factor = 0.1
    decay_factor = 0.7
    iteration = 30

    result_dir = "results"
    fname = file_path.split("/")[-1].split(".")[0]  # 文件名前綴, e.g. graph_1

    graph = init_graph(file_path)

    graph.display()

    output_HITS(iteration, graph, result_dir, fname)
    output_PageRank(iteration, graph, damping_factor, result_dir, fname)
    output_SimRank(iteration, graph, decay_factor, result_dir, fname)
