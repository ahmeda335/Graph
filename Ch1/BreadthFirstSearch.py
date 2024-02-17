import numpy as np
from UndirectedGraph import ListOfListsGraph
from mystack import Stack
from myqueue import Queue


My_Graph = ListOfListsGraph(4)
My_Graph.add_edge(0, 1)
My_Graph.add_edge(0, 2)
My_Graph.add_edge(2, 1)
My_Graph.add_edge(2, 3)

stack = Stack()
queue = Queue()


# This will give me all the vertices of a Graph using BFS (Bridth First Search).
class BFS:
    def __init__(self, graph):
        self._queue = queue
        self._stack = stack
        self.marked = np.full(graph.V, False, dtype=bool)
        self.edge_to = np.full(graph.V, 0, dtype=int)
        self.distance_to = np.full(graph.V, 'inf', dtype=float)

    def printing_graph_using_BFS(self, graph, starting_point):
        print(starting_point)
        self.BFS(graph, starting_point)

    def BFS(self, graph, starting_point):
        self.distance_to[starting_point] = 0
        self.marked[starting_point] = True
        self._queue.enqueue(starting_point)
        while not self._queue.is_empty():
            v = self._queue.dequeue()
            for w in graph.adjacents(v):
                if not self.marked[w]:
                    self.edge_to[w] = starting_point
                    self.distance_to[w] = self.distance_to[v] + 1
                    self.marked[w] = True
                    self._queue.enqueue(w)
                    print(w)


# This will give me the smallest path from one point to another using BFS.
class DistanceToUsingBFS:
    def __init__(self, graph):
        self._queue = queue
        self._stack = stack
        self.marked = np.full(graph.V, False, dtype=bool)
        self.edgeTo = np.full(graph.V, 0, dtype=int)
        self.distTo = np.full(graph.V, 'inf', dtype=float)

    # returning the smallest distance between two vertices.
    def distance_to(self, graph, starting_point, end_point):
        self.BFS(graph, starting_point)
        print(f"The smallest distance between {starting_point} and {end_point} is: {int(self.distTo[end_point])}")

    def BFS(self, graph, starting_point):
        self.distTo[starting_point] = 0
        self.marked[starting_point] = True
        self._queue.enqueue(starting_point)
        while not self._queue.is_empty():
            v = self._queue.dequeue()
            for w in graph.adjacents(v):
                if not self.marked[w]:
                    self.edgeTo[w] = starting_point
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    self._queue.enqueue(w)


if __name__ == '__main__':
    my_bfs = BFS(My_Graph)
    my_bfs.printing_graph_using_BFS(My_Graph, 0)

    my_bfs2 = DistanceToUsingBFS(My_Graph)
    my_bfs2.distance_to(My_Graph, 0, 3)


