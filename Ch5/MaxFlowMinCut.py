#           flow/capacity
#    v  ------- 7/9 -------> w
#
#
#      Forward edge(capacity - flow)
#      -------- 2 --------->
#    v                        w
#      <-------- 7 ---------
#      Backward edge(flow)
#

from Ch1.myqueue import Queue
import random


class FlowEdge:
    def __init__(self, v, w, capacity, flow):
        """
        initializes an edge from vertex 'v' to vertex 'w' with the given capacity and flow.
        :param v: the start of the edge.
        :param w: the end of the edge.
        :param capacity: the capacity of the edge.
        :param flow: the flow of the edge.
        """
        if (v or w) < 0:
            raise ValueError("vertex can't be negative.")
        if capacity < 0:
            raise ValueError("Edge capacity can't be negative.")
        self.start = v
        self.end = w
        self.capacity = capacity
        self.flow = flow

    def From(self):
        return self.start

    def To(self):
        return self.end

    def Capacity(self):
        return self.capacity

    def Flow(self):
        return self.flow

    def other(self, vertex):
        """
        - Returns the end point of the edge that is different from the given vertex.
        :param vertex: one endpoint of the edge.
        :return: the other endpoint of the edge.
        """
        if vertex == self.start:
            return self.end
        elif vertex == self.end:
            return self.start
        else:  # if the vertex is not one of the endpoints.
            raise ValueError("Illegal endpoint")

    def residual_capacity_to(self, vertex):
        """
        - Returns the residual capacity of the edge in the direction of the given vertex.
        :param vertex: one endpoint of the edge.
        :return: the residual capacity of the edge in the direction of the given vertex
        """
        if vertex == self.start:
            return self.flow
        elif vertex == self.end:
            return self.capacity - self.flow
        else:  # The vertex is not endpoint.
            raise ValueError("Illegal End Point")

    def add_residual_flow_to(self, vertex, delta):
        """
        - Increase the flow on the edge in the direction of the given vertex.
        :param vertex: endpoint of the edge.
        :param delta: the amount by which to increase the flow.
        :return: None.
        """
        if delta < 0:
            raise ValueError("delta can't be negative")

        if vertex == self.start:
            self.flow -= delta
        elif vertex == self.end:
            self.flow += delta
        else:
            raise ValueError("Illegal endpoint")

        if not(0 <= self.flow <= self.capacity):
            raise ValueError("flow can't be negative or greater than capacity")

    def to_string(self):
        return self.start + " -> " + self.end + ", " + "flow/capacity: " + self.flow + "/" + self.capacity


class FlowNetwork:
    """
    - This class represents capacitated network with vertices 'V' and a directed edges, each edge is of
    type flow edge and has a capacity and flow.
    - self-loops and parallel edges are permitted.
    - It supports the following two primary operations: add an edge to the network,
    and iterate over all of the edges incident to or from a vertex.
    """
    def __init__(self, v):
        """
        - Initializes an empty flow network with 'v' vertices and 0 edges.
        :param v: number of the flow network vertices.
        """
        if v < 0:
            raise ValueError("Number of vertices can't be negative.")
        self.V = v
        self.edges = 0
        self.adj = [[] for i in range(self.V)]  # The adj of vertices are edges.

    # Add an edge to the network
    def add_edge(self, edge):
        """
        - Adding edge to the network
        """
        v = edge.From()
        w = edge.To()
        self.is_valid_vertex(v)
        self.is_valid_vertex(w)
        self.adj[v].append(edge)
        self.adj[w].append(edge)
        self.edges += 1

    # Initializing random flow network
    def random_weighted_network(self, edges):
        """
        - Initializing a random edge weighted graph.
        :param edges: Number of edges wanted to be added to the graph.
        :return: None.
        """
        if edges < 0:
            raise ValueError("Number of edges can't be negative.")
        for i in range(edges):
            v = random.randint(0, self.V - 1)
            w = random.randint(0, self.V - 1)
            capacity = random.randint(0, 10)
            flow = random.randint(0, capacity)
            e = FlowEdge(v, w, capacity, flow)
            self.add_edge(e)

    # Initializing a wighted edge from the user.
    def input_weighted_network(self):
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
                        if 0 <= v < self.V:
                            break
                        else:
                            print("Please enter a valid vertex")
                    break
                except ValueError:
                    print("Please Enter integer numbers.")
            while True:
                try:
                    while True:
                        w = int(input("Input the other vertex: "))
                        if 0 <= v < self.V:
                            break
                        else:
                            print("Please, enter a valid vertex.")
                    break
                except ValueError:
                    print("Please Enter integer numbers.")
            while True:
                try:
                    capacity = float(input("Input the edge's capacity: "))
                    break
                except ValueError:
                    print("Please Enter a valid capacity.")
            while True:
                try:
                    while True:
                        flow = float(input("Input the edge's flow: "))
                        if flow > capacity:
                            print("Flow can't be bigger than capacity, please write a valid value.")
                        else:
                            break
                    break
                except ValueError:
                    print("Please Enter a valid flow.")

            edge = FlowEdge(v, w, capacity, flow)
            self.add_edge(edge)

    # Return the incident edges to a vertex either to or from that vertex.
    def adjacents(self, v):
        """
        - Returns the edges incident to a vertex 'v' including both edges pointing to
        and from the vertex.
        :param v: the vertex
        :return: the edges incident to the vertex.
        """
        return self.adj[v]

    # Return the number of vertices.
    def vertices(self):
        return self.V

    # Return the number of edges.
    def edges(self):
        return self.edges

    # # If there is a path from vertex to a vertex.
    # def hasPathTo(self, v1, v2):
    #     for edge in self.Adjacents(v1)
    #         if

    # Does the network contain the vertex.
    def is_valid_vertex(self, v):
        if v < 0 or v >= self.V:
            raise ValueError(f"Vertex {v} is not between zero and {self.V - 1}")

    # Printing the Network
    def print_the_network(self):
        print(f"Number of vertices is: {self.V}, and number of edges is: {self.edges}.")
        print("\nthe edge in the format (other vertex, flow, capacity)")
        for v in range(self.V):
            adjacent_edges = []
            for edge in self.adjacents(v):
                if edge.To() != v:
                    adjacent_edges.append((edge.To(), edge.Flow(), edge.Capacity()))
            print(v, " : ", *adjacent_edges)


class FordFulkerson:
    """
    - This class represents a data type for computing a maximum s-t flow and a minimum s-t cut
    in a flow network.
    """
    def __init__(self, network, s, t):
        """
        - Computes the maximum flow and the minimum cut of a network from vertex 's' to vertex 't'.
        :param network: the given network.
        :param s: the start vertex.
        :param t: the end(sink) vertex.
        """
        self.network = network
        self.V = network.vertices()

        self.is_valid_vertex(s)
        self.is_valid_vertex(t)
        if s == t:
            raise "The source equal the sink."
        self.s = s
        self.t = t
        self.marked = [False for i in range(self.V)]
        self.edgeTo = [None for i in range(self.V)]  # The last edge to the vertex.
        self.Max_Flow = 0  # Current value of Max Flow.
        self.FF()

    def FF(self):
        """
        - This is the main function that will be executed when calling this class
        - It finds both MaxFlow and MinCut.
        - Then we can print MaxFlow value using 'print_max_flow' and MiniCut vertices
          using 'print_min_cut_vertices'.
        """
        self.Max_Flow = self.excess(self.t)
        while self.has_augmenting_path():

            # compute bottleneck capacity.
            bottle = float('inf')  # bottle is considered the path of the flow.
            v = self.t
            while v != self.s:
                bottle = min(bottle, self.edgeTo[v].residual_capacity_to(v))
                v = self.edgeTo[v].other(v)

            # Augment flow.
            v = self.t
            while v != self.s:
                self.edgeTo[v].add_residual_flow_to(v, bottle)
                v = self.edgeTo[v].other(v)

            self.Max_Flow += bottle
        print("\nFinished Getting MaxFlow and MinCut")

    # If there is an augmenting path.
    def has_augmenting_path(self):
        self.marked = [False for i in range(self.V)]
        self.edgeTo = [None for i in range(self.V)]  # The last edge to the vertex.

        queue = Queue()
        queue.enqueue(self.s)
        self.marked[self.s] = True
        while (not queue.is_empty()) and (not self.marked[self.t]):
            v = queue.dequeue()
            for edge in self.network.adjacents(v):
                w = edge.other(v)
                if (edge.residual_capacity_to(w) > 0) and (not self.marked[w]):
                    self.edgeTo[w] = edge
                    self.marked[w] = True
                    queue.enqueue(w)

        # True if there is an augmenting path.
        return self.marked[self.t]

    # return excess flow at vertex v.
    def excess(self, v):
        excess = 0
        for edge in self.network.adjacents(v):
            if v == edge.From():
                excess -= edge.Flow()
            else:
                excess += edge.Flow()
        return excess

    # Returns the value of the maximum flow.
    def value(self):
        return self.Max_Flow

    # The vertex is in the side of the mincut or no.
    def inCut(self, v):
        """
        :param v: the vertex
        :return: True -> if the vertex is in the side of the mincut.
                 False -> otherwise.
        """
        self.is_valid_vertex(v)
        return self.marked[v]

    # Does the network contain the vertex.
    def is_valid_vertex(self, v):
        if v < 0 or v >= self.V:
            raise ValueError(f"Vertex {v} is not between zero and {self.V - 1}")

    # Print Max Flow
    def print_max_flow(self):
        print("--> It is in the form (start, end, flow, capacity)")
        print(f"- Max Flow from {self.s} to {self.t} is: ", end='')
        for v in range(self.V):
            for edge in self.network.adjacents(v):
                if v == edge.From() and edge.Flow() > 0:
                    print("(" + str(edge.From()) + ', ' + str(edge.To()) + ', ' + str(edge.Flow()) + ', ' + str(edge.Capacity()) + ")", end=" ")
        print("\n- Max Flow Value: ", self.Max_Flow)

    def print_min_cut_vertices(self):
        mincut_vertices = []
        for v in range(self.V):
            if self.inCut(v):
                mincut_vertices.append(v)
        print("- The Min Cut vertices are: ", mincut_vertices)


if __name__ == '__main__':
    flow_network = FlowNetwork(10)
    flow_network.random_weighted_network(20)
    flow_network.print_the_network()
    ff = FordFulkerson(flow_network, 0, 9)
    ff.print_max_flow()
    ff.print_min_cut_vertices()
    #####
    #
    # flow_network2 = FlowNetwork(4)
    # flow_network2.input_weighted_network()
    # flow_network2.print_the_network()
    # ff2 = FordFulkerson(flow_network2, 0, 3)
    # ff2.print_max_flow()
    # ff2.print_min_cut()




