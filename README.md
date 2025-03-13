The files with the suffix solver are not the decision problems but rather Search problems.

Clique solver finds a solution given an adjacency matrix and a constant k by reducing it to SAT. we use a SAT solver from pysat

Independent set solver reduces to clique solver.

vertex cover solver reduces to Independent set solver. (buggy)
