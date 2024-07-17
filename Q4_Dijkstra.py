# O((V + E) log V) using heap
# O(V^2)
def dijkstra(V, graph, S):
    dist = [float('inf')] * V
    dist[S] = 0
    visited = [False] * V

    for _ in range(V):
        min_dist = float('inf')
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1: 
            break

        visited[u] = True
        
        for v, wt in graph[u]:
            if not visited[v] and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    return dist


V = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

graph = [[] for _ in range(V)]
for _ in range(edges):
    u, v, wt = map(int, input("Enter edge (u, v, wt): ").split())
    graph[u - 1].append((v - 1, wt))  

source = int(input("Enter the source vertex: ")) - 1 
dist = dijkstra(V, graph, source)

print("Shortest distances from source vertex:", dist)
