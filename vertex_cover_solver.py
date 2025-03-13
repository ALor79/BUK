# Falsche Reduktion
from independent_set_solver import independetSetOfSize
import numpy as np # type: ignore

def vertexCoverOfSize(adj,k):
    n = len(adj)
    complement_of_result = independetSetOfSize(adj,n-k)
    if complement_of_result is None:
        return None
    result=[]
    for i in range(0,n):
        if i not in complement_of_result:
            result.append(i)
    return result

if __name__ == '__main__':
    # Example graph: 5 vertices with the following adjacency matrix.
    # (A 1 indicates an edge between vertices, 0 indicates no edge.)
    # adj = [
    #     [0, 1, 0, 1, 0],  # Vertex 1 is connected to 2 and 4.
    #     [1, 0, 1, 0, 1],  # Vertex 2 is connected to 1, 3, and 5.
    #     [0, 1, 0, 1, 0],  # Vertex 3 is connected to 2 and 4.
    #     [1, 0, 1, 0, 1],  # Vertex 4 is connected to 1, 3, and 5.
    #     [0, 1, 0, 1, 0]   # Vertex 5 is connected to 2 and 4.
    # ] case k=2
    adj =[
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0]
        ]

    # We are looking for a clique of size k = 2.
    k = 2
    
    vertex_cover = vertexCoverOfSize(adj, k)
    if vertex_cover:
        print("vertex_cover of size", k, "found:",list(map(lambda x: x + 1, vertex_cover))) 
    else:
        print("No vertex_cover of size", k, "exists in the graph.")