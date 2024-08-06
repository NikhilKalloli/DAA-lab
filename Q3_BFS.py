#  Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges in the graph.
def bfs(graph, source, visited):

    queue = [source]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node, end=' ')
            visited.append(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

graph = {}

nodes = int(input("Enter the total number of nodes: "))
for i in range(nodes):
    key = input("Enter the key: ")
    value = set(input(f"Enter the nodes connected to {key} (space-separated): ").split())
    graph[key] = value

    for v in value:
        if v not in graph:
            graph[v] = set()

print("Graph:", graph)

source = input("Enter the start node for BFS: ")
visited = set()
print("Source node", source, "using BFS:")
bfs(graph, source, visited)
