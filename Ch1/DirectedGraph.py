import numpy as np

#  O(E + V) -> Big-Oh notation.


class AdjMatrixGraph:
    """
    - The Graph is implemented as a boolean values in a square matrix of rows equal columns equal
    number of vertices.

    - If there is an edge from v1 -> v2, we put True at only adj[v1][v2].

    - This type of graph doesn't allow parallel edges, but self-loops are allowed.

    - When creating objects, number of the graph vertices is required.
    """

    # Empty graph with V vertices.
    def __init__(self, v):
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.V = v  # number of vertices
        self.E = 0  # number of edges.
        self.adj = np.full((self.V, self.V), False, dtype=bool)   # Creating a square matrix with rows and columns = 'self.V'
                                                                  # and with 'False' default value

    # Directed Edge from v -> w.
    def add_edge(self, v, w):
        """
        Adding Edge to the graph. The order of the vertices is important.
        :param v: The starting point of the edge.
        :param w: The end point of the edge.
        :return: None.
        """
        if (v or w) > self.V:
            raise ValueError("Invalid numbers")
        if not(self.adj[v][w]):
            self.E += 1
        self.adj[v][w] = True

    # Returning number of vertices.
    def vertices_number(self):
        return self.V

    # Returning number of Edges.
    def edges_number(self):
        return self.E

    # Returning the inner degree of the vertices.
    def indegree(self, v):  # I made this method using different way in the second class.
        """
        - The indegree of a vertex is the number of edges this vertex is
        end-point at.
        :param v: The required vertex to know its indegree.
        :return: The indegree of 'v' vertex.
        """
        count = 0
        for i in range(self.V):
            if self.adj[i][v]:
                count += 1
        return count

    # Returning the outer degree of the vertices.
    def outdegree(self, v):
        """
        - The outdegree of a vertex is the number of edges this vertex is
        a starting point at.
        :param v: The required vertex to know its outdegree.
        :return: The outdegree of 'v' vertex.
        """
        count = 0
        for i in range(self.V):
            if self.adj[v][i]:
                count += 1
        return count

    # Does the graph contain the edge v -> w.
    def does_contain(self, v, w):
        """
        - The order of (v, w) are important. The edge is from v -> w.
        :param v: The starting point of the edge.
        :param w: The end-point of the edge.
        :return: True or False
        """
        return self.adj[v][w]

    # Return the vertices that I can reach from v.
    def adjacents(self, v):
        """
        - If I have an edge v -> w, I can reach 'w' from 'v' but I can't reach 'v' from 'w'.
        :param v: The vertex wanted to get its adjacents.
        :return: adjacensts of 'v' vertex.
        """
        neighbours = []
        for w in range(self.V):
            if self.adj[v][w]:
                neighbours.append(w)
        return neighbours

    # Printing the Graph
    def print_the_graph(self):
        print(f"Number of vertices is: {self.V}, and number of edges is: {self.E}.")
        for v in range(self.V):
            adjacents = []
            for w in range(self.V):
                if self.does_contain(v, w):
                    adjacents.append(str(w))
            adjacents_string = ', '.join(adjacents)
            print(f"We can go from vertex {v} to the vertices : {adjacents_string}")


##############################################################################################


class ListOfListsGraph:
    """
    - The Graph is emplemented as a list of 'V' elements, each element is a list.

    - If there is an adge from v1 -> v2, so we append only 'v2' to adj[v1].

    - Both parallel edges and self-loops are allowed in this type of graph.

    - When creating objects, number of the graph vertices is required.
    """

    # Empyth graph with V vertices.
    def __init__(self, v):
        if v < 0:
            raise ValueError("Number of vertices can't be negative")
        self.V = v  # number of vertices
        self.E = 0  # number of edges.
        self.adj = [[] for i in range(v)]  # creating a list of v elements.
        self.indegree = np.full(self.V, 0, dtype=int)  # I use this variable to count the vertex indegree.

    # Add directed edge v -> w
    def add_edge(self, v, w):
        """
        Adding Edge to the graph. The order of the vertices is important.
        :param v: The starting point of the edge.
        :param w: The end-point of the edge.
        :return: None.
        """
        if (v or w) > self.V:
            raise ValueError("Invalid numbers")
        self.E += 1
        self.adj[v].append(w)
        self.indegree[w] += 1

    # Returning number of vertices.
    def vertices_number(self):
        return self.V

    # Returning number of Edges.
    def edges_number(self):
        return self.E

    # Returning the outdegree of the vertices.
    def outdegree(self, v):
        """
        - The outdegree of a vertex is the number of edges this vertex is
        a starting point at.
        :param v: The required vertex to know its outdegree.
        :return: The outdegree of 'v' vertex.
        """
        return len(self.adj[v])

    # Returning the indegree of a vertex
    def Indegree(self, v):
        """
        - The indegree of a vertex is the number of edges this vertex is
        end-point at.
        :param v: The required vertex to know its indegree.
        :return: The indegree of 'v' vertex.
        """
        return self.indegree[v]

    # Does the graph contain the vertex.
    def is_valid_vertex(self, v):
        return v <= self.V

    # Does the graph contain the edge v -> w.
    def does_contain(self, v, w):
        """
        - The order of (v, w) are important. The edge is from v -> w.
        :param v: The starting point of the edge.
        :param w: The end-point of the edge.
        :return: True or False
        """
        for i in range(len(self.adj[v])):
            if w == self.adj[v][i]:
                return True
        return False

    # Return the vertices that I can reach from v.
    def adjacents(self, v):
        """
        - If I have an edge v -> w, I can reach 'w' from 'v' but I can't reach 'v' from 'w'.
        :param v: The vertex wanted to get its adjacents.
        :return: adjacensts of 'v' vertex.
        """
        neighbours = []
        for i in range(len(self.adj[v])):
            neighbours.append(self.adj[v][i])
        return neighbours

    # Printing the DirectedGraph
    def print_the_graph(self):
        print(f"Number of vertices is: {self.V}, and number of edges is: {self.E}.")
        for v in range(self.V):
            adjacents = []
            for i in range(len(self.adj[v])):

                adjacents.append(str(self.adj[v][i]))
            adjacents_string = ', '.join(adjacents)
            print(f"We can go from vertex {v} to the vertices : {adjacents_string}")

    # Printing the reverse Graph.
    # Note: If we reversed the graph, we have the same strongly connected components.
    def reverse_graph(self):
        reverse = ListOfListsGraph(self.V)
        for v in range(self.V):
            for i in range(len(self.adj[v])):
                reverse.add_edge(self.adj[v][i], v)
        return reverse


#############################################################################################

if __name__ == '__main__':
    My_Graph = AdjMatrixGraph(7)
    My_Graph.add_edge(0, 1)
    My_Graph.add_edge(0, 2)
    My_Graph.add_edge(2, 1)
    My_Graph.add_edge(2, 3)
    My_Graph.add_edge(4, 5)
    My_Graph.add_edge(5, 1)
    My_Graph.add_edge(6, 4)

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

    print("*" * 50)

    My_Graph.reverse_graph().print_the_graph()
    print(My_Graph.does_contain(0, 1))
    print(My_Graph.does_contain(3, 0))
    print(My_Graph.edges_number())
    print(My_Graph.vertices_number())
    print(My_Graph.adjacents(2))
