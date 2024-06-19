def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_spanning_tree = []
    min_edge = [float('inf')] * n
    min_edge[0] = 0

    for _ in range(n):
        u = min((i for i in range(n) if not visited[i]), key=lambda x: min_edge[x])
        visited[u] = True
        min_spanning_tree.append((u, min_edge[u]))

        for v, weight in enumerate(graph[u]):
            if not visited[v] and weight < min_edge[v]:
                min_edge[v] = weight

    return min_spanning_tree

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

min_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in min_spanning_tree:
    print(edge)