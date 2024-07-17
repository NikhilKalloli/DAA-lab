#  O(V * E)
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

V = (int(input("enter the no. of vertex: ")))
E = (int(input("enter the no. of edges: ")))

edges = []
for i in range(E):

    u, v, wt = input("Enter edge (u, v, wt): ").split()
    wt=int(wt)
    u=ord(u)-ord('a')
    v=ord(v)-ord('a')
    edges.append((u, v, wt))

    
source = input("Enter the source vertex: ")
source=ord(source)-ord('a')
dist = bellman_ford(V, edges, source)
    
print(dist)