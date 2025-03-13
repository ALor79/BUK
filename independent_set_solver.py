from clique_solver import cliqueOfSize
import numpy as np # type: ignore

def independetSetOfSize(adj,k):
    """
    Given an adjacency matrix for an undirected graph with n vertices,
    and an integer k, this function constructs a clique that computes that
    the graph has a independent set of size k.
    Returns a list of vertices (1-indexed) forming a Independent Set of size k, or None if no such Independent Set exists.
    """
    n=len(adj)
    # declare the complement matrix
    complement_matrix = [[0] * n for _ in range(n)]

    # invert values of the adjacency matrix and store them in the complement matrix
    for row in range(n):
        for col in range(n):
            if row != col:
                complement_matrix[row][col]=not adj[row][col]

    result = cliqueOfSize(complement_matrix,k)
    return result

if __name__ == '__main__':
    # Example graph: 5 vertices with the following adjacency matrix.
    # (A 1 indicates an edge between vertices, 0 indicates no edge.)
    adj =[
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0]
    ]
    
    k = 4
    
    independent_set = independetSetOfSize(adj, k)
    if independent_set:
        print("Independent set of size", k, "found:",list(map(lambda x: x + 1, independent_set)) )
    else:
        print("No independent set of size", k, "exists in the graph.")

