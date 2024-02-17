import random


# Defining a weighted edge
class Edge:
    """
    - This is no directed edge, but I used "edge_start" & "edge_end"
      to differentiate between them.
    """
    def __init__(self, v, w, weight):
        """
        - Creating an edge.
        :param v: One end-point of the edge.
        :param w: The other end-point of the edge.
        :param weight: The weight of the edge.
        """
        if (v or w) < 0:
            raise ValueError("vertex can't be negative")
        self.edge_start = v
        self.edge_end = w
        self.weight = weight

    def weight(self):
        return self.weight

    # returning one of the edge vertices
    def one_vertex(self):
        return self.edge_start

    # returning the other vertex
    def other_vertex(self, vertex):
        if vertex == self.edge_start:
            return self.edge_end
        else:
            return self.edge_start


# Defining the weighted Graph.
class EdgeWeightedGraph:
    """
    - The Weighted Graph in this class is make using list of lists. If I want to use Adjacent matrix,
    the value of the matrix will be the weight of the edge, and at no edge, it will be zero.
    """

    # Empyth graph with V vertices.
    def __init__(self, v):
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.verticesNum = v  # number of vertices
        self.edgesNum = 0  # number of edges.
        self.adj = [[] for i in range(self.verticesNum)]  # creating a list of v elements.

    def random_weighted_graph(self, edges):
        """
        - Initializing a random edge weighted graph.
        :param edges: Number of edges wanted to be added to the graph.
        :return: None.
        """
        for i in range(edges):
            v = random.randint(0, self.verticesNum - 1)
            w = random.randint(0, self.verticesNum - 1)
            weight = round(random.uniform(0.00, 100.00), 2)
            e = Edge(v, w, weight)
            self.add_edge(e)

    # Initializing a wighted edge from the user.
    def input_weighted_graph(self):
        while True:
            try:
                edges = int(input("Write the number of edges: "))
                break
            except ValueError:
                print("Invalid input, write an integer number.")
        print("Type vertex 1 as a start vertex not 0")
        for i in range(edges):
            print(f"Edge {i + 1}: ")
            while True:
                try:
                    v = int(input("Input edge's vertex: ")) - 1
                    break
                except ValueError:
                    print("Please Enter integer numbers.")
            while True:
                try:
                    w = int(input("Input the other vertex: ")) - 1
                    break
                except ValueError:
                    print("Please Enter integer numbers.")
            while True:
                try:
                    weight = float(input("Input the edge's weight: "))
                    break
                except ValueError:
                    print("Please Enter a valid weight.")
            edge = Edge(v, w, weight)
            self.add_edge(edge)

    # Adding an edge to the graph.
    def add_edge(self, edge):
        v = edge.one_vertex()
        w = edge.other_vertex(v)
        self.adj[v].append(edge)  # Each vertex is a list containing the edges connected to that vertex.
        self.adj[w].append(edge)  # Each vertex is a list containing the edges connected to that vertex.
        self.edgesNum += 1

    # Returning number of vertices.
    def vertices_number(self):
        return self.verticesNum

    # Returning number of Edges.
    def edges_number(self):
        return self.edgesNum

    # Returning the degree of the vertices.
    def degree(self, v):
        return len(self.adj[v])

    # Does the graph contain the vertex.
    def is_valid_vertex(self, v):
        return v <= self.verticesNum

    # Return list of neighbours of v.
    def adjacents(self, v):
        return self.adj[v]

    # Return the edges of the graph.
    def edges(self):
        edges = []
        for v in range(self.verticesNum):
            selfloops = 0
            for e in self.adj[v]:
                if e.other_vertex(v) > v:
                    edges.append(e)
                elif e.other_vertex(v) == v:
                    if selfloops % 2 == 0:
                        edges.append(e)
                    selfloops += 1
        return edges

    # printing the weights of the edges
    def weights(self):
        weights = self.edges()
        for i in weights:
            print(f"The weight of the edge {i.one_vertex()} - {i.other_vertex(i.one_vertex())} is {i.weight}")

    # Printing the Graph
    def print_the_graph(self):
        print(f"Number of vertices is: {self.verticesNum}, and number of edges is: {self.edgesNum}.")
        for v in range(self.verticesNum):
            adjacent_edges = []
            for i in self.adj[v]:
                adjacent_edges.append((i.other_vertex(v), i.weight))
            print(v, " : ", *adjacent_edges)


if __name__ == '__main__':
    myedge = EdgeWeightedGraph(10)
    myedge.random_weighted_graph(20)
    myedge.print_the_graph()
    myedge.weights()

