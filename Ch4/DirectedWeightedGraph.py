# The Directed weighted Graph is a graph that its edges are directed and with a weight.

import random


class DirectedEdge:
    """
    - The Directed Edge is an edge with start point 'v' and endpoint 'w' and
    has a weight on it.
    """
    def __init__(self, v, w, weight):
        """
        - The order is important 'v' is the starting point, and 'w' is the endpoint.
        """
        self.startingPoint = v
        self.endPoint = w
        self.weight = weight

    def From(self):
        """
        :return: It returns 'one_vertex' in the weighted Graph.
        """
        return self.startingPoint

    def To(self):
        """
        :return: It returns 'the_other_vertex' in the weighted Graph.
        """
        return self.endPoint

    def Weight(self):
        return self.weight


class EdgeWeightedDirectedGraph:
    """
    - The Weighted Graph in this class is implemented using list of lists. If I want to use Adjacent matrix,
    the value of the matrix will be the weight of the edge. If the edge is from v -> w, the value of
    (v, w) will be the weight of the edge, and the value of (w, v) will be zero because it is directed
    graph. We put zero at no edge.
    - The user enters the starting vertex '0' not '1'.
    """
    def __init__(self, v):
        """
        :param v: The number of the graph vertices.
        """
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.verticesNum = v
        self.edgesNum = 0  # The number of the graph edges with initial value zero.
        self.adj = [[] for i in range(self.verticesNum)]

    def add_edge(self, edge):
        v = edge.From()
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.adj[v].append(edge)
        self.edgesNum += 1

    def adjacents(self, v):
        """
        :return: The incident edges to the vertex 'v'.
        """
        return self.adj[v]

    def random_weighted_graph(self, edges):
        """
        - Initializing a random edge weighted directed graph.
        :param edges: Number of edges wanted to be added to the graph.
        :return: None.
        """
        for i in range(edges):
            v = random.randint(0, self.verticesNum - 1)
            w = random.randint(0, self.verticesNum - 1)
            weight = round(random.uniform(0.00, 100.00), 2)
            edge = DirectedEdge(v, w, weight)
            self.add_edge(edge)

    # Initializing a wighted graph from the user.
    def input_weighted_graph(self):
        while True:
            try:
                edges = int(input("Write the number of edges: "))
                break
            except ValueError:
                print("Invalid input, write an integer number.")
        print("\nNote: Type vertices to start from index '0' not index '1'")
        for i in range(edges):
            print(f"Edge {i}: ")
            while True:
                try:
                    while True:
                        v = int(input("Input edge's vertex: "))
                        if 0 <= v < self.verticesNum:
                            break
                        else:
                            print("Please enter a valid vertex.")
                    break
                except ValueError:
                    print("Please Enter integer numbers.")
            while True:
                try:
                    while True:
                        w = int(input("Input the other vertex: "))
                        if 0 <= w < self.verticesNum:
                            break
                        else:
                            print("Please enter a valid vertex.")
                    break
                except ValueError:
                    print("Please Enter integer numbers.")
            while True:
                try:
                    weight = float(input("Input the edge's weight: "))
                    break
                except ValueError:
                    print("Please Enter a valid weight.")
            edge = DirectedEdge(v, w, weight)
            self.add_edge(edge)

    # Returning the number of vertices.
    def vertices_number(self):
        return self.verticesNum

    # Returning the number of edges.
    def edges_number(self):
        return self.edgesNum

    # Returning the degree of the vertices.
    def degree(self, v):
        return len(self.adj[v])

    # Return the edges of the graph.
    def edges(self):
        edges = []
        for v in range(self.verticesNum):
            for e in self.adj[v]:
                edges.append(e)
        return edges

    # printing the weights of the edges
    def weights(self):
        all_edges = self.edges()
        for edge in all_edges:
            print(f"The weight of the edge {edge.From()} - {edge.To()} is {edge.Weight()}")

    # Printing the Graph
    def print_the_graph(self):
        print(f"Number of vertices is: {self.verticesNum}, and number of edges is: {self.edgesNum}.")
        for v in range(self.verticesNum):
            adjacent_edges = []
            for edge in self.adj[v]:
                adjacent_edges.append((edge.To(), edge.Weight()))
            print(v, " : ", *adjacent_edges)


if __name__ == '__main__':
    directed_weighted_graph = EdgeWeightedDirectedGraph(10)
    directed_weighted_graph.random_weighted_graph(20)
    directed_weighted_graph.print_the_graph()

    # directed_weighted_graph2 = EdgeWeightedDirectedGraph(4)
    # directed_weighted_graph2.input_weighted_graph()
    # directed_weighted_graph2.print_the_graph()
