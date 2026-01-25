## Dijkstra's Shortest Path Algorithm
## Single source to all nodes
## Graph should not have negative weights
## TC: O(ELogV), SC: O(V+E)
import heapq

from graphs.graph import Graph 

def dijkstra(graph: list[list[int]], src: int) -> list[int]:
    n = len(graph)
    dist = [float("inf")] * n
    dist[src] = 0
    h = [(0, src)]
    while h:
        w, node = heapq.heappop(h)
        if dist[node] < w:
            continue
        for nbr, wt in graph[node]:
            if dist[nbr] > w + wt:
                dist[nbr] = w + wt
                heapq.heappush(h, (dist[nbr], nbr))
    return dist

if __name__ == "__main__":
    edges = [[0, 1, 10], [1, 2, 100], [0, 2, 50], [2, 5, 76], [2, 3, 23], [2, 4, 89], [0, 4, 78], [1, 4, 1], [0, 5, 85]]
    g = Graph(V = 6, edges=edges)
    src = 0
    dist = dijkstra(graph=g.adjacency_list, src=src)
    print("Shortest path from " + str(src) + " to all nodes")
    for i, d in enumerate(dist):
        print(str(src) + " to " + str(i) + ": " + str(d))