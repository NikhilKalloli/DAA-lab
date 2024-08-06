def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


nodes = int(input("Enter number of nodes: "))
graph ={}

for i in range(nodes):
    key = input("Enter Node: ")
    value = set(input("Enter connected vertices: ").split())
    graph[key] = value

    for v in value:
        if v not in graph:
            graph[v]  = set()

start = input("Enter start vertex: ")
visited = set()
dfs(graph, start, visited)