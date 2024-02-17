# Goal: Find the MST using Prim's Algorithm.
# Prim's Algorithm is a special case of Greedy Algorithm.
# Steps:
# 1) Start from vertex '0', and find the smallest edge in weight that is one endpoint in T.
# 2) Find the smallest edge is done using Priority Queue. 'Lazy Implementation'
#    - All the edges are put in the priority queue and are ordered based on their weight.
#    - These edges must be one endpooint in T, which mean that one of the edge vertices must be in the T.
#    - Delete-min to determine next edge to add to T.
#    - If the edges's two vertices are in the T, we disregard it to prohibit cycles.
#    - Otherwise, let w be the vertex not in T:
#        * add to PQ any edge incident to w (assuming other point not in T)
#        * add w to T.

from PriorityQueue import PriorityQueue
import heapq
from Ch1.WeightedGraph import EdgeWeightedGraph


class LazyPrimMST:
    def __init__(self, graph):
        self.weightedGraph = graph
        self.mst = []
        self.minPQ = []
        self.marked = [False] * self.weightedGraph.vertices_number()

    def prim(self):
        self.visit(0)
        while len(self.minPQ) > 0:
            edge = heapq.heappop(self.minPQ)[1]
            v = edge.one_vertex()
            w = edge.other_vertex(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.append(edge)
            if not self.marked[v]:
                self.visit(v)
            if not self.marked[w]:
                self.visit(w)

    def visit(self, vertex):
        self.marked[vertex] = True
        for edge in self.weightedGraph.adjacents(vertex):
            if not self.marked[edge.other_vertex(vertex)]:
                heapq.heappush(self.minPQ, (edge.weight, edge))  # I entered a tuple from the edge weight and the edge
                                                        # as the PQ compares the weights and I then can retrieve the edge.

    def print_MST(self):
        print("The MST is:")
        for i in range(len(self.mst)):
            edge = self.mst[i]
            print(f"{edge.one_vertex()} - {edge.other_vertex(edge.one_vertex())}"
                  f" with weight: {edge.weight}")


if __name__ == '__main__':
    mygraph = EdgeWeightedGraph(10)
    mygraph.random_weighted_graph(20)
    mygraph.print_the_graph()
    lazyprimMST = LazyPrimMST(mygraph)
    lazyprimMST.prim()
    lazyprimMST.print_MST()


# - Prim's Algorithm builds MST in time proportional to O(E*logE) in the worst case. But with using
#   HeapPriorityQueue not ordinary one. I used ordinary one.

# - We can implement the Prim's Algorithm using also method called Eager Implementation.
