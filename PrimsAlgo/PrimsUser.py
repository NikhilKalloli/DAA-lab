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

# Take user input for the graph
num_nodes = int(input("Enter the total number of nodes: "))
num_edges = int(input("Enter the total number of edges: "))

graph = {i: [] for i in range(num_nodes)}

print("Enter the edges in the format: u v weight")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))

start = int(input("Enter the starting node: "))
minimum_cost = prims_algorithm(graph, start)
print(f"The minimum cost to cover all locations is: {minimum_cost}")
