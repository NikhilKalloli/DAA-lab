def prim(V, adj, start):
   
    dist = [float('inf')] * V
    dist[start] = 0
    visited = [False] * V
    
    mst_cost = 0
    
    for _ in range(V):
        min_weight = float('inf')
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < min_weight:
                min_weight = dist[i]
                u = i
        
        if u == -1:
            break
        
        visited[u] = True
        mst_cost += min_weight
        
        for v, wt in adj[u]:
            if not visited[v] and wt < dist[v]:
                dist[v] = wt
    
    return mst_cost

V = int(input("Enter Number od Vertices: "))
edges = int(input("Enter number od edges: "))
adj = [[] for _ in range(V)]

for i in range(edges):
    u, v, wt = map(int, input("Enter (u,v,wt): ").split())
    adj[u].append([v, wt])
    adj[v].append([u, wt])


start_vertex = 0 

mst_cost = prim(V, adj, start_vertex)
print("Minimum Cost of Spanning Tree:", mst_cost)
