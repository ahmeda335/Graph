# Creating MST(Minimum Spanning Tree) using Kruskal's method.

# The method of creating MST using Kruskal's Algorithm is:
# 1) The graph edges are ordered in an ascending order depending on its weight.
# 2) we go through the edges from smaller to bigger and put it in the MST, but
#    with condition that when the edge is put, it doesn't create a cycle in
#    the MST.

# Note: Number of MST edges = Graph Vertices - 1

from Ch1.WeightedGraph import EdgeWeightedGraph
from Ch1.myqueue import Queue
from UnionFind import *


def smart_bubble_sort(lst):
    """
    - This function is specifically used to order the edges of the weighted graph
    depending on their weights.
    - Bubble Sort is not the most efficient way of sorting, I can use any other method
    like SelectionSort, MergeSort, or QuickSort. But I used smart-bubble-sort in this case.
    """
    exchanges = True
    for i in range(len(lst) - 1):
        if not exchanges:
            break
        exchanges = False
        for j in range(len(lst) - 1 - i):
            if lst[j].weight > lst[j + 1].weight:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                exchanges = True
    return lst


class KruskalMST:
    def __init__(self, graph):
        self.weightedGraph = graph
        self.verticesNum = graph.vertices_number()
        self.mst = []
        self.UF = DisjSet(self.verticesNum)

    def getting_mst(self):
        edges = []
        for edge in self.weightedGraph.edges():
            edges.append(edge)
        edges = smart_bubble_sort(edges)  # This will order the edges depending on their weights
        for i in range(len(edges)):
            e = edges[i]
            v = e.one_vertex()
            w = e.other_vertex(v)
            if not self.UF.connected(v, w):
                self.UF.union(v, w)
                self.mst.append(e)

    # Printing the MST
    def print(self):
        print("The MST is:")
        for i in range(len(self.mst)):
            edge = self.mst[i]
            print(f"{edge.one_vertex()} - {edge.other_vertex(edge.one_vertex())}"
                  f" with weight: {edge.weight}")


if __name__ == '__main__':
    mygraph = EdgeWeightedGraph(10)
    mygraph.random_weighted_graph(20)
    mygraph.print_the_graph()
    mst = KruskalMST(mygraph)
    mst.getting_mst()
    mst.print()


# - Kruskal Algorithm builds MST in time proportional to O(E*logE) in the worst case. But with using
#   HeapPriorityQueue not ordinary one. I used ordinary one.
