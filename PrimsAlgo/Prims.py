# Time Complexity: O(E logV) where V is the number of vertices and E is the number of edges in the graph.

import heapq
def prims_algorithm(graph, start):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return total_cost

# Define the graph as an adjacency list
# Each pair (v, weight) in the adjacency list means there is an edge from u to v with the given weight
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}

start = 0
minimum_cost = prims_algorithm(graph, start)
print(f"The minimum cost to cover all locations is: {minimum_cost}")