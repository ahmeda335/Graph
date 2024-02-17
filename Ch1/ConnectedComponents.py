import UndirectedGraph
import DirectedGraph
import numpy as np


class ConnectedComponents:
    """
    - This class returns the number of connected components in a Graph, and
    informs you if two vertices are strongly connected or not.
    - We can handle it to print these connected components.
    """
    def __init__(self, graph):
        self._count = 0
        self.marked = np.full(graph.V, False, dtype=bool)
        self.component = np.full(graph.V, 0, dtype=int)  # Determines the component of each vertex.

    def dfs(self, graph, s):
        self.marked[s] = True
        self.component[s] = self._count
        for w in graph.adjacents(s):
            if not self.marked[w]:
                self.dfs(graph, w)

    def number_of_connected_components(self, graph):
        """
        :return: The number of connected components found in this graph.
        """
        for i in range(graph.V):
            if not self.marked[i]:
                self.dfs(graph, i)
                self._count += 1
        return self._count

    def vertices_components(self):
        """
        :return: The components of each vertex found in the graph in the shape of list.
        """
        return self.component

    def is_strongly_connected_components(self, v, w):
        """
        - In undirected graph, two vertices are strongly connected components if there
        is a path between them.
        :param v: First vertex
        :param w: Second Vertex
        :return: If the two vertex are strongly connected components or not 'True or False'.
        """
        return self.component[v] == self.component[w]

    # TODO: Implementing this class to the directed graph. It is done using Kosaraju-Sharir Algorithm.


if __name__ == '__main__':
    My_Undirected_Graph = UndirectedGraph.AdjMatrixGraph(8)
    My_Undirected_Graph.add_edge(0, 1)
    My_Undirected_Graph.add_edge(0, 2)
    My_Undirected_Graph.add_edge(2, 1)
    My_Undirected_Graph.add_edge(2, 3)
    My_Undirected_Graph.add_edge(4, 5)
    My_Undirected_Graph.add_edge(6, 7)

    My_Directed_Graph = DirectedGraph.AdjMatrixGraph(13)
    My_Directed_Graph.add_edge(0, 1)
    My_Directed_Graph.add_edge(0, 5)
    My_Directed_Graph.add_edge(2, 0)
    My_Directed_Graph.add_edge(2, 3)
    My_Directed_Graph.add_edge(3, 2)
    My_Directed_Graph.add_edge(3, 5)
    My_Directed_Graph.add_edge(4, 2)
    My_Directed_Graph.add_edge(4, 3)
    My_Directed_Graph.add_edge(5, 4)
    My_Directed_Graph.add_edge(6, 0)
    My_Directed_Graph.add_edge(6, 4)
    My_Directed_Graph.add_edge(6, 8)
    My_Directed_Graph.add_edge(6, 9)
    My_Directed_Graph.add_edge(7, 6)
    My_Directed_Graph.add_edge(7, 9)
    My_Directed_Graph.add_edge(8, 6)
    My_Directed_Graph.add_edge(9, 10)
    My_Directed_Graph.add_edge(9, 11)
    My_Directed_Graph.add_edge(10, 12)
    My_Directed_Graph.add_edge(11, 4)
    My_Directed_Graph.add_edge(11, 12)
    My_Directed_Graph.add_edge(12, 9)

    CC = ConnectedComponents(My_Undirected_Graph)
    print(CC.number_of_connected_components(My_Undirected_Graph))
    print(CC.vertices_components())
    print(CC.is_strongly_connected_components(0, 3))
    print(CC.is_strongly_connected_components(0, 5))
