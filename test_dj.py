import heapq

def dijkstra(graph, src):
    V = len(graph)
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist


V = int(input("Enter number of locations: "))
graph = [[] for _ in range(V)]
for _ in range(int(input("Enter the number of roads: "))):
    u, v, w = map(int, input("Enter road (start, end, distance): ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

src = int(input("Enter starting location: "))

distances = dijkstra(graph, src)

print("Location Distance from start")
for i, d in enumerate(distances):
    print(f"{i}\t\t{d}")
