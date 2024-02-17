####
####
# Topological sort is done when I want to know the sequence of an operation.
# For example, I have a graph which determines the sequence of learning some track.
# Let us say, that to learn Artificial Intelligence, you must learn
# 1) Simple Programming.
# 2) Python Language.
# 3) Algorithms.
# 4) Some of Maths and Statistics
# so The graph is
# Simple Programming -> Python language -> Algorithms -> Maths and Statistics -> AI
# ----- Note -----
# Topological sort is only done on DAG (Directed Acyclic Graph)
# It is obvious that the graph can be drawn in only one direction.
####
####
# ----- Another Example -----
# 0) Algorithms.
# 1) Complexity Thory.
# 2) Artificial Intelligence.
# 3) Intro to CS.
# 4) Cryptography.
# 5) Scientific Computing.
# 6) Advanced Programming.
######
# 0 -> 5      0 -> 2
# 0 -> 1      3 -> 6
# 3 -> 5      3 -> 4
# 5 -> 4      6 -> 4
# 6 -> 0      3 -> 2
# 1 -> 4
####################################
####################################
from Ch1.DirectedGraph import ListOfListsGraph
import numpy as np
from Ch1.mystack import Stack


class TopologicalSort:
    def __init__(self, graph):
        self.graph = graph
        self.marked = np.full(graph.vertices_number(), False, dtype=bool)
        self.reversePost = Stack()  # Initializing an object from the Stack class
        self.V = graph.vertices_number()
        self.counter = 0

    def get_topological_sort(self):
        self.depth_first_order()
        return self.reverse_post()

    def depth_first_order(self):
        for v in range(self.V):
            if not self.marked[v]:
                self.dfs(v)

    def dfs(self, v):
        self.marked[v] = True
        for w in self.graph.adjacents(v):
            if not self.marked[w]:
                self.dfs(w)
        self.reversePost.push(v)
        self.counter += 1

    def reverse_post(self):
        """
        Due to DFS the result is reversed, so this function is used to
        output the result in the right order using the stack.
        """
        order = []
        for i in range(self.counter):
            order.append(self.reversePost.pop())
        return order
        # print(*order, sep=" -> ")


if __name__ == '__main__':
    My_Graph = ListOfListsGraph(7)
    My_Graph.add_edge(0, 5)
    My_Graph.add_edge(0, 2)
    My_Graph.add_edge(0, 1)
    My_Graph.add_edge(3, 6)
    My_Graph.add_edge(3, 5)
    My_Graph.add_edge(3, 4)
    My_Graph.add_edge(5, 4)
    My_Graph.add_edge(6, 4)
    My_Graph.add_edge(6, 0)
    My_Graph.add_edge(3, 2)
    My_Graph.add_edge(1, 4)

    TS = TopologicalSort(My_Graph)
    print(TS.get_topological_sort())


# We see that the output is:
# 3 -> 6 -> 0 -> 1 -> 2 -> 5 -> 4
# This means that this is the map that we must follow to learn all branches.
