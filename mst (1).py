# Define infinity as a large number
INF = 9999999

# Define a function to print the MST
# Define a function to print the MST and its cost
def print_mst(parent, graph):
    print("Edge \tWeight")
    cost = 0 # Initialize cost variable
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
        cost += graph[i][parent[i]] # Add edge weight to cost
    print("Minimum cost:", cost) # Print the total cost


# Define a function to find the vertex with minimum key value
def min_key(key, mst_set):
    mn = INF
    for v in range(V):
        if key[v] < mn and mst_set[v] == False:
            mn = key[v]
            min_index = v
    return min_index

# Define a function to implement prim's algorithm
def prim_mst(graph):
    # Array to store constructed MST
    parent = [None] * V
    # Key values used to pick minimum weight edge in cut
    key = [INF] * V
    # To represent set of vertices not yet included in MST
    mst_set = [False] * V
    # Include first vertex in MST
    key[0] = 0
    parent[0] = -1 # First node is always root of MST
    # The MST will have V vertices
    for _ in range(V):
        # Pick the minimum key vertex from the set of vertices not yet included in MST
        u = min_key(key, mst_set)
        # Add the picked vertex to the MST Set
        mst_set[u] = True
        # Update key value and parent index of the adjacent vertices of the picked vertex.
        # Consider only those vertices which are not yet included in MST
        for v in range(V):
            # graph[u][v] is non zero only for adjacent vertices of u
            # mstSet[v] is false for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if graph[u][v] > 0 and mst_set[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
    # Print the constructed MST
    print_mst(parent, graph)

# Driver code

# Ask user for number of vertices and edges
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

# Create a 2D array of size V x V for adjacency matrix to represent graph
graph = [[0 for _ in range(V)] for _ in range(V)]

# Ask user for edge details and fill the adjacency matrix
for _ in range(E):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    graph[u][v] = w
    graph[v][u] = w # Assuming undirected graph

# Apply prim's algorithm on the graph
prim_mst(graph)
