def bellman_ford(V, edges, S):
    dist = [float('inf')] * V
    dist[S] = 0

    for i in range(V - 1):
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    for u, v, wt in edges:
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            print("-ve cycle.")
            return [-1]

    return dist

v = (int(input("enter the no. of vertex: ")))
e = (int(input("enter the no. of edges: ")))

edges = []
for i in range(e):
    edge = list(map(int, input("enter edge (u, v, wt): ").split()))
    edges.append(edge)
    
source = 0
dist = bellman_ford(v, edges, source)
    
print(dist)