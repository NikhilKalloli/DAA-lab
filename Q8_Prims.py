def prim(V, edges, start):
    adj = [[] for _ in range(V)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    
    min_edge = [float('inf')] * V
    min_edge[start] = 0
    in_mst = [False] * V
    mst_cost = 0
    
    for _ in range(V):
        min_weight = float('inf')
        u = -1
        for v in range(V):
            if not in_mst[v] and min_edge[v] < min_weight:
                min_weight = min_edge[v]
                u = v
        
        if u == -1:
            break
        
        in_mst[u] = True
        mst_cost += min_weight
        
        for v, wt in adj[u]:
            if not in_mst[v] and wt < min_edge[v]:
                min_edge[v] = wt
    
    return mst_cost

V = 5  
edges = [
    (0, 1, 5),
    (1, 2, 20),
    (1, 3, 10),
    (3, 4, 5),
    (2, 4, 1)
]
start_vertex = 0 

mst_cost = prim(V, edges, start_vertex)
print("Minimum Cost of Spanning Tree:", mst_cost)