
def dijkstra(source , graph, V):
    dist = [float('inf')]*V
    visited = [False]*V
    dist[source]  = 0

    for _ in range(V):
        min_dist = float('inf')
        u = -1

        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u==-1: break

        visited[u] = True

        for v,wt in graph[u]:
            if not visited[v] and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    return dist 




V = int(input("Enter Vertices: "))
edges = int(input("Enter edges: "))

graph = [[] for _ in range(V)]

for _ in range(edges):
    u, v, wt = map(int, input("Enter (u,v,wt): ").split())
    graph[u-1].append((v -1, wt))


source = int(input("Enter source: ")) -1

# print(graph)
dist = dijkstra(source, graph, V)

print(dist)

