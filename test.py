def dijkstra(V, adj, S):
    dist = [float('inf')] * V
    dist[S] = 0
    visited = [False] * V

    for _ in range(V):
        # Find the vertex with the minimum distance that hasn't been processed yet
        min_dist = float('inf')
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        # If no vertex was found, break (this happens when remaining vertices are unreachable)
        if u == -1:
            break

        # Mark the vertex as processed
        visited[u] = True
        
        # Relaxation step
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    return dist


# Input
V = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

graph = [[] for _ in range(V)]
for _ in range(edges):
    u, v, wt = map(int, input("Enter edge (u, v, wt): ").split())
    graph[u - 1].append((v - 1, wt))  

source = int(input("Enter the source vertex: ")) - 1 
dist = dijkstra(V, graph, source)

print("Shortest distances from source vertex:", dist)
