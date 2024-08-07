def find(parent, i):
    if parent[i]==i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot]  =yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot]+=1



def kruskal(edges, V):
    parent =[]
    rank = []

    edges.sort(key = lambda x: x[2])
    for node in range(V):
        parent.append(node)
        rank.append(0)

    mst_cost =0
    mst_edges =[]

    for u,v,wt in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x!=y:
            mst_cost+=wt
            mst_edges.append([u,v,wt])
            union(parent, rank, x, y)
    
    return mst_cost, mst_edges





V = int(input("Enter vertices: "))
num = int(input("ENter number of edges: "))
edges= []

for i in range(num):
    u, v ,wt = map(int,  input("Enter (u,v,wt): ").split())
    edges.append([u,v,wt])

cost , min_edges  = kruskal(edges, V)
print("cost: ", cost)
print(min_edges)
