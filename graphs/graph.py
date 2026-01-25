class Graph:
    def __init__(self, V: int = 100, edges: list[list[int]] = None, is_directed : bool = False) -> None:
        self.V = V
        self.edges = edges
        self.is_directed = is_directed

        self.adjacency_list = self._build_adj()
        self.adj_matrix = self._build_mat()
        
    def _build_adj(self):
        g = [[] for _ in range(self.V)]
        for a, b, w in self.edges:
            g[a].append((b, w))
            if not self.is_directed:
                g[b].append((a, w))
        return g
    
    def _build_mat(self):
        m = [[0 for _ in range(self.V)] for _ in range(self.V)]
        for a, b, w in self.edges:
            m[a][b] = w
            if not self.is_directed:
                m[b][a] = w
        return m
                


        