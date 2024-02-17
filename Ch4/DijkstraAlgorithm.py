# Note: Dijkstra Algorithm and Prim's Algorithm are essentially the same Algorithm.
#       Both are in the family of algorithms that compute the family spanning trees.
# Main Distinction is: Rule used to choose next vertex to the tree.
#     Prim's: Closeset vertex to the tree (via an undirected edge)
#     Dijkstra's: Closest vertex to the source (via an directed edge)

# Note: Dijkstra Algorithm works only with positive weight edges.
# If I have negative weight edges, I use another Algorithm called Bellman-Ford Algorithm
# Dijkstra -> uses Greedy Approach.
# Bellman-Ford -> uses Dynamic Programming Approach.


from DirectedWeightedGraph import EdgeWeightedDirectedGraph
from IndexedMinPQ import IndexedMinPQ
from Ch1.mystack import Stack


class DijkstraSP:
    """
    - Dijkstra Algorithm is used to get the shortest path between two points in a graph.
    - The user enter graph with vertices starting from vertex '0' not '1'.
    """
    def __init__(self, graph, s):
        self.directedWG = graph
        self.verticesNum = graph.vertices_number()
        self.start = s
        self.edgeTo = [None for i in range(self.verticesNum)]
        self.distTo = []
        self.pq = IndexedMinPQ(self.verticesNum)

        # setting the initial distances 'infinity' other than the start 'zero'.
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
        self.dijkstraSP()
        self.print_path(target)

    def dijkstraSP(self):
        self.pq.insert(self.start, 0)
        while not self.pq.isEmpty():
            v = self.pq.deleteMin()[0]
            for edge in self.directedWG.adjacents(v):
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
            if self.pq.Contain(w):
                self.pq.decreaseKey(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])

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


if __name__ == '__main__':
    # directed_weighted_graph = EdgeWeightedDirectedGraph(10)
    # directed_weighted_graph.random_wighted_graph(20)
    # sp = DijkstraSP(directed_weighted_graph, 0)
    # sp.GettingSP()
    # sp.printPath(5)

    vertices = int(input("Write the number of vertices: "))
    directed_weighted_graph2 = EdgeWeightedDirectedGraph(vertices)
    directed_weighted_graph2.input_weighted_graph()
    start = int(input("Write the start vertex: "))
    sp2 = DijkstraSP(directed_weighted_graph2, start)
    goal = int(input("Write the vertex you want its SP: "))
    sp2.getting_SP(goal)


# The Worst case depends on the type of Periority Queue used.
# Unordered Array: V^2
# Binary Heap: E logV
# There are two other types of PQ: d-way Heap and Fibonacci Heap. They are much faster.


