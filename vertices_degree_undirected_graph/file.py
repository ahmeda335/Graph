def compute_vertex_degrees(pairs):
    degrees = {}

    for pair in pairs:
        u = pair[0]
        v = pair[1]

        # Update for vertex u
        if u in degrees:
            degrees[u] += 1
        else:
            degrees[u] = 1

        # Update for vertex v
        if v in degrees:
            degrees[v] += 1
        else:
            degrees[v] = 1

    # Printing the degrees of each vertex.
    print("Degrees of each vertex:")
    for vertex in sorted(degrees):
        print("Vertex", vertex, "has degree", degrees[vertex])
    # Printing edges
    print("\n\nEdges in the graph:")
    for pair in pairs:
        print(f"{pair[0]} -- {pair[1]}")
        

if __name__ == '__main__':
    pairs = [
    (1, 2),
    (2, 3),
    (1, 3),
    (3, 4),
    (4, 5),
    (1, 5)
    ]  

    compute_vertex_degrees(pairs)
