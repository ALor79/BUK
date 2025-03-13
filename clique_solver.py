from pysat.solvers import Minisat22 # type: ignore
from pysat.formula import CNF # type: ignore

def cliqueOfSize(adjacency_matrix, k):
    """
    Given an adjacency matrix (list of lists) for an undirected graph with n vertices,
    and an integer k, this function constructs a SAT formula that is satisfiable if and only if
    the graph has a clique of size k.
    Returns a list of vertices (1-indexed) forming a clique of size k, or None if no such clique exists.
    """
    n = len(adjacency_matrix)  # Number of vertices in G
    num_vars = k * n           # We will have k positions, each with n possible vertices.
    
    cnf = CNF()

    # 1. At least one vertex is assigned to each clique position.
    for i in range(1, k + 1):
        clause = []
        for j in range(1, n + 1):
            # x_{i,j} is represented as variable number: (i-1)*n + j
            clause.append((i - 1) * n + j)
        cnf.append(clause)
    
    # 2. At most one vertex is assigned to each clique position.
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(j + 1, n + 1):
                var1 = (i - 1) * n + j
                var2 = (i - 1) * n + l
                cnf.append([-var1, -var2])
    
    # 3. Each vertex appears in at most one position.
    for j in range(1, n + 1):
        for i in range(1, k + 1):
            for l in range(i + 1, k + 1):
                var1 = (i - 1) * n + j
                var2 = (l - 1) * n + j
                cnf.append([-var1, -var2])
    
    # 4. Non-adjacency constraint: if vertices u and v are not adjacent in G, then they cannot both be in the clique.
    # For every pair of clique positions (i, l) with i < l, and for every pair of vertices (u, v)
    # such that u != v and there is no edge between u and v, add the clause: not(x_{i,u}) or not(x_{l,v}).
    for i in range(1, k + 1):
        for l in range(i + 1, k + 1):
            for u in range(1, n + 1):
                for v in range(1, n + 1):
                    if u != v and adjacency_matrix[u - 1][v - 1] == 0:
                        var1 = (i - 1) * n + u
                        var2 = (l - 1) * n + v
                        cnf.append([-var1, -var2])
    
    # Use a SAT solver (Minisat22) to solve the CNF formula.
    with Minisat22(bootstrap_with=cnf) as solver:
        if not solver.solve():
            return None  # No clique of size k exists.
        model = solver.get_model()
    
    # Decode the model: for each clique position i, find a vertex j such that x_{i,j} is true.
    clique = []
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            var = (i - 1) * n + j
            if var in model:
                clique.append(j-1)
                break
                
    return clique

# -----------------------------
# Example test case:
# -----------------------------
if __name__ == '__main__':
    # Example graph: 5 vertices with the following adjacency matrix.
    # (A 1 indicates an edge between vertices, 0 indicates no edge.)
    adjacency_matrix = [
        [0, 1, 0, 0, 0],  # Vertex 1 is connected to 2, 4
        [1, 0, 1, 1, 1],  # Vertex 2 is connected to 1, 3, 4, 5
        [0, 1, 0, 0, 0],  # Vertex 3 is connected to 2
        [1, 1, 0, 0, 1],  # Vertex 4 is connected to 1 ,2, 5
        [0, 1, 0, 1, 0]   # Vertex 5 is connected to 2, 4
    ]
    
    # We are looking for a clique of size k = 3.
    k = 3
    
    clique = cliqueOfSize(adjacency_matrix, k)
    if clique:
        print("Clique of size", k, "found:",list(map(lambda x: x + 1, clique)) )
    else:
        print("No clique of size", k, "exists in the graph.")
