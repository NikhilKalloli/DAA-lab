def tsp(graph, v, curr_pos, n, count, cost, min_cost):
    if count == n and graph[curr_pos][0]:
        min_cost[0] = min(min_cost[0], cost + graph[curr_pos][0])
        return

    for i in range(n):
        if v[i] == False and graph[curr_pos][i]:
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[curr_pos][i], min_cost)
            v[i] = False

n = 4
graph = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]
    
v = [False for i in range(n)]
v[0] = True
min_cost = [float('inf')]
    
tsp(graph, v, 0, n, 1, 0, min_cost)
    
print("The minimum cost is", min_cost[0])