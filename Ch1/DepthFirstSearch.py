from mystack import Stack
import numpy as np
from UndirectedGraph import AdjMatrixGraph


# This will give the place from any vertex to all other vertices.
class DFS:
    def __init__(self, graph):
        self._stack = Stack()  # Intitializing an object from the stack class.
        self._count = 0
        self.graph = graph
        # Initializing a list to know if the vertex is marked or know.
        self.marked = np.full(graph.V, False, dtype=bool)
        # Initializing a list to know if there is edges between two vertices.
        self.edge_to = np.full(graph.V, 0, dtype=int)

    def dfs(self, start_point):
        """
        - Traversing through the graph using DFS.
        :param start_point: The starting point I want to make DFS from.
        """
        self.marked[start_point] = True
        for w in self.graph.adjacents(start_point):
            if not self.marked[w]:
                self.edge_to[w] = start_point   # I use this if I want to get the path from one point to another.
                self.dfs(w)
                print(f"{w} from: {self.edge_to[w]}")

    def getting_graph(self, v):
        if self.graph.is_valid_vertex(v):
            self.dfs(v)
            print(f"{v} from: {self.edge_to[v]}")


class Path:
    """# Does the graph contain the vertex.
    def is_valid_vertex(self, v):
        return self.V >= v > 0
    - Getting the path from one point to another.
    """
    def __init__(self, graph):
        self._stack2 = Stack()  # Intitializing an object from the stack class.
        self._count = 0
        self.graph = graph
        self.marked = np.full(graph.V, False, dtype=bool)
        self.edge_to = np.full(graph.V, 0, dtype=int)

    def path_to(self, start_point, end_point):
        self.marked[start_point] = True
        for w in self.graph.adjacents(start_point):
            if not self.marked[w]:
                self.marked[w] = True
                self.edge_to[w] = start_point
                self._stack2.push(start_point)
                if w == end_point:
                    self._stack2.push(end_point)
                    self.marked[end_point] = True
                    return 0
                self.path_to(w, end_point)

    def getting_path(self, start_point, end_point):
        mylst = []
        self.path_to(start_point, end_point)
        while self._stack2.peek() != start_point:
            mylst.append(self._stack2.pop())
        mylst.append(start_point)
        return mylst

    def printing_the_path(self, start_point, end_point):
        revlst = self.getting_path(start_point, end_point)
        revlst.reverse()
        print(*revlst, sep=" -> ")


if __name__ == '__main__':
    My_Undirected_Graph = AdjMatrixGraph(8)
    My_Undirected_Graph.add_edge(0, 1)
    My_Undirected_Graph.add_edge(0, 2)
    My_Undirected_Graph.add_edge(2, 1)
    My_Undirected_Graph.add_edge(2, 3)
    My_Undirected_Graph.add_edge(3, 4)
    My_Undirected_Graph.add_edge(4, 5)
    My_Undirected_Graph.add_edge(6, 7)

    # Traversing the graph from vertex '0'.
    my_dfs = DFS(My_Undirected_Graph)
    my_dfs.dfs(0)
    my_dfs.getting_graph(0)

    # Getting the path from vertex'1' to vertex '3'.
    my_dfs2 = Path(My_Undirected_Graph)
    my_dfs2.printing_the_path(1, 5)
