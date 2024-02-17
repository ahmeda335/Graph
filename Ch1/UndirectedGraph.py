import numpy as np

# - O (E + V)  -> Big-Oh notation.


class AdjMatrixGraph:
    """
    - The Graph is emplemented as a boolean values in a square matrix of rows equal columns equal
    number of vertices.

    - If there is an edge between two vertices, let's say (v1, v2), so we put True at both
    adj[v1][v2] & adj[v2][v1].

    - The adjacent matrix is symmetric for the undirected graph, A = A(Transpose).

    - This type of graph doesn't allow parallel edges, but self-loops are allowed.

    - I can allow paralled edges, but the values of the adjacent matrix will be numbers (1, 2, ...)
    depending on the paralled edges number instead of boolean values (True, False).

    - When creating objects, number of the graph vertices is required.

    """

    # Empty graph with V vertices.
    def __init__(self, v) -> int:
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.V = v  # number of vertices
        self.E = 0  # number of edges.
        self.adj = np.full((self.V, self.V), False, dtype=bool)    # Creating a square matrix with rows and columns = 'self.V'
                                                                   # and with 'False' default value

    # Add undirected edge v-w.
    def add_edge(self, v, w):
        if (v or w) > self.V:
            raise ValueError("Invalid numbers")
        if not(self.adj[v][w]):  # If there is no edge found.
            self.E += 1
        self.adj[v][w] = True
        self.adj[w][v] = True

    # Returning number of vertices.
    def vertices_number(self):
        return self.V

    # Returning number of Edges.
    def edges_number(self):
        return self.E

    # Returning the degree of the vertices.
    def degree(self, v) -> int:
        count = 0
        for i in range(self.V):
            if self.adj[v][i]:
                count += 1
        return count

    # Does the graph contain the edge v-w.
    def does_contain(self, v, w):
        return self.adj[v][w]

    # Return list of neighbours of v.
    def adjacents(self, v):
        neighbours = []
        for i in range(self.V):
            if self.adj[v][i]:
                neighbours.append(i)
        return neighbours

    # Does the graph contain the vertex.
    def is_valid_vertex(self, v):
        return self.V >= v > 0

    # Printing the Graph
    def print_the_graph(self):
        print(f"Number of vertices is: {self.V}, and number of edges is: {self.E}.")
        for v in range(self.V):
            adjacents = []
            for w in range(self.V):
                if self.does_contain(v, w):
                    adjacents.append(str(w))
            adjacents_string = ', '.join(adjacents)
            print(f"The vertex {v} is connected to the vetices : {adjacents_string}")


# List of lists graph.
class ListOfListsGraph:
    """
    - The Graph is emplemented as a list of 'V' elements, each element is a list.

    - If there is an edge between two vertices, let's say (v1, v2), so we append 'v2'
    to adj[v1], and append 'v1' to adj[v2].

    - Both parallel edges and self-loops are allowed in this type of graph.

    - When creating objects, number of the graph vertices is required.
    """

    # Empty graph with V vertices.
    def __init__(self, v):
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.V = v  # number of vertices
        self.E = 0  # number of edges.
        self.adj = [[] for i in range(v)]  # creating a list of v elements.

    # Add undirected edge v-w.
    def add_edge(self, v, w):
        if (v or w) > self.V:
            raise ValueError("Invalid numbers")
        self.E += 1
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Returning number of vertices.
    def vertices_number(self):
        return self.V

    # Returning number of Edges.
    def edges_number(self):
        return self.E

    # Returning the degree of the vertices.
    def degree(self, v):
        return len(self.adj[v])

    # Does the graph contain the vertex.
    def is_valid_vertex(self, v):
        return self.V >= v > 0

    # Does the graph contain the edge v-w.
    def does_contain(self, v, w):
        for i in range(len(self.adj[v])):
            if w == self.adj[v][i]:
                return True
        return False

    # Return list of neighbours of v.
    def adjacents(self, v):
        neighbours = []
        for i in range(len(self.adj[v])):
            neighbours.append(self.adj[v][i])
        return neighbours

    # Printing the Graph
    def print_the_graph(self):
        print(f"Number of vertices is: {self.V}, and number of edges is: {self.E}.")
        for v in range(self.V):
            adjacents = []
            for i in range(len(self.adj[v])):
                adjacents.append(str(self.adj[v][i]))
            adjacents_string = ', '.join(adjacents)
            print(f"The vertex {v} is connected to the vertices : {adjacents_string}")


# Note: You notice that you don't have any information about the nodes or the edges, you can only know
#       the adjacent nodes of a node or the edges connected to nodes. But if I want to add information
#       for the nodes and the edges. I can make this using another two matrices (Node Feature Matrix,
#       Edge Feature Matrix). They are used more in Graphic Neural Networks.
#      TODO: Design a graph with information for the nodes and the edges.
#############################################################################################


if __name__ == '__main__':
    My_Graph = AdjMatrixGraph(4)
    My_Graph.add_edge(0, 1)
    My_Graph.add_edge(0, 2)
    My_Graph.add_edge(2, 1)
    My_Graph.add_edge(2, 3)
    My_Graph.print_the_graph()
    print(My_Graph.does_contain(0, 1))
    print(My_Graph.does_contain(3, 0))
    print(My_Graph.edges_number())
    print(My_Graph.vertices_number())
    print(My_Graph.adjacents(2))

    print("*" * 50)

    My_Graph = ListOfListsGraph(6)
    My_Graph.add_edge(0, 1)
    My_Graph.add_edge(0, 2)
    My_Graph.add_edge(2, 1)
    My_Graph.add_edge(2, 3)
    My_Graph.add_edge(4, 5)

    My_Graph.print_the_graph()
    print(My_Graph.does_contain(0, 1))
    print(My_Graph.does_contain(3, 0))
    print(My_Graph.edges_number())
    print(My_Graph.vertices_number())
    print(My_Graph.adjacents(2))
    print(My_Graph.adj)
