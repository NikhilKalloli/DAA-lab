#  Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges in the graph.
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node) 
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

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

visited = set()  
start_node = input("Enter the start node for DFS: ")
dfs_recursive(graph, start_node, visited)
