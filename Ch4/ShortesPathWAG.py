# - If the Weighted Directed Graph is Acyclic(no cycles) like topological order,
# I can make a simpler Algorithm to obtain the shortest path between two points.

# - I will use Topological Sort in this Algorithm.

# - Topological Sort Algorithm computes SPT in any edge weighted DAG in time
# proportional to E + V.

# - Each edge e = v -> w is relaxed exactly once (when v is relaxed), leaving
# distTo[w] <= distTo[v] + e.weight().

# - This Algorithm allows negative weights, so I can negate all the weights and
# get the longes path using the same algorithm.

from Ch1.TopologicalSort import TopologicalSort
from DirectedWeightedGraph import EdgeWeightedDirectedGraph
from Ch1.mystack import Stack


class AcyclicSP:
    """
    - AcyclicSP Algorithm is used to get the shortest path between two points
    in an acyclic graph using Topological Sort.
    - The user enters graph with vertices starting from index '0' not index '1'.
    """
    def __init__(self, graph, s):
        self.graph = graph
        self.verticesNum = graph.vertices_number()
        self.start = s
        self.edgeTo = [None for i in range(graph.vertices_number())]
        self.distTo = []

        # Setting the initial distances from the start vertex 'infinity' rather than the start 'zero'.
        for i in range(self.verticesNum):
            self.distTo.append(float('inf'))
        self.distTo[self.start] = 0.0

    def getting_SP(self, target):
        """
        - The main funciton that gets the shortest path between the start
        and a target, then printing this short path.
        :param target: the point you want to get the short path to.
        :return: getting the shortest path, then printing it.
        """
        self.topological_sort()
        self.print_path(target)

    def topological_sort(self):
        topological = TopologicalSortV2(self.graph)  # Creating object from 'TopologicalSortV2' class
        verticess = topological.get_topological_sort()
        for vertex in verticess:
            for edge in self.graph.adjacents(vertex):
                self.relax(edge)

    def relax(self, edge):
        """
        - This funciton makes sure that you get the shortest path.
        """
        v = edge.From()
        w = edge.To()
        if self.distTo[w] > self.distTo[v] + edge.weight:
            self.distTo[w] = self.distTo[v] + edge.weight
            self.edgeTo[w] = edge

    def dist_to(self, v):
        """
        :return: The distance between the start and a vertex 'v' if found.
        """
        self.is_valid_vertex(v)
        if self.has_path_to(v):
            return self.distTo[v]
        else:
            return f"There is no path from vertex {self.start} to vertex {v}"

    def has_path_to(self, v):
        """
        - Find if there is a path from the start to vertex 'v'.
        """
        self.is_valid_vertex(v)
        return self.distTo[v] < float('inf')

    def path_to(self, v):
        self.is_valid_vertex(v)
        if not self.has_path_to(v):
            return None
        path = Stack()
        edge = self.edgeTo[v]
        while edge:
            path.push(edge)
            edge = self.edgeTo[edge.From()]
        return path

    def print_path(self, v):
        path = self.path_to(v)
        if path is not None:
            print(f"The shortest path from {self.start} to {v} is ", end=' ')
            while not path.is_empty():
                if path.size() > 1:
                    print(path.pop().From(), " -> ", end=" ")
                else:
                    print(path.peek().From(), " -> ", path.pop().To(), end="  ")
            print(f"with weight {self.distTo[v]}")
        else:
            print("No path found")

    def is_valid_vertex(self, v):
        if v < 0 or v >= self.verticesNum:
            raise ValueError(f"vertex {v} is not between 0 and {self.verticesNum}")


class TopologicalSortV2(TopologicalSort):
    """
    - I made this inheritance from the original Topological Sort, because the adjacents of the vertics
    in the weighted graph are edges, then I must handle the dfs to take only the end-point vertex from
    the edge not all the edge.
    """
    def __init__(self, graph):
        TopologicalSort.__init__(self, graph)

    def dfs(self, v):
        self.marked[v] = True
        for w in self.graph.adjacents(v):
            if not self.marked[w.To()]:
                self.dfs(w.To())
        self.reversePost.push(v)
        self.counter += 1


if __name__ == '__main__':
    vertices = int(input("Write the number of vertices: "))
    directed_weighted_graph2 = EdgeWeightedDirectedGraph(vertices)
    directed_weighted_graph2.input_weighted_graph()
    start = int(input("Write the start vertex: "))
    sp2 = AcyclicSP(directed_weighted_graph2, start)
    goal = int(input("Write the vertex you want its SP: "))
    sp2.getting_SP(goal)


# It takes O(E + V)
