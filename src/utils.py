import numpy as np
import os

from .graph import Graph
from .HITS import HITS
from .PageRank import PageRank
from .Similarity import Similarity
from .SimRank import SimRank


# 初始化 graph，
# 包括讀 .txt 檔與建立 Graph
def init_graph(fname):
    # 讀.txt檔

    with open(fname) as f:
        lines = f.readlines()

    # 定義 graph = Graph()
    graph = Graph()

    # 分割每行的數據
    # 建立成 graph
    if fname == "dataset/ibm-5000.txt":
        # ibm-5000.txt檔處理方式
        for line in lines:
            parts = line.split()

            parent = int(parts[-2])  # 倒數第二個值
            child = int(parts[-1])  # 倒數第一個值
            graph.add_edge(parent, child)
    else:
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
    print("SimRank:")
    print("[")
    for row in ans_metrix:
        print(row)
    print("]")

    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)

    np.savetxt(
        os.path.join(path, fname + simrank_fname),
        np.asarray(ans_metrix, dtype="float32"),
        fmt="%.3f",
        newline="\n",
    )
