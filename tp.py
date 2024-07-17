def knapsack(weights, values, capacity):
    n = len(values)
    
    # Create a 2D list to store the maximum value for each weight capacity
    # order of matrix (n + 1) x (capacity + 1)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (capacity + 1))
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    # Find which items are included in the optimal solution
    w = capacity
    items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i)
            w -= weights[i-1]

    return dp[n][capacity], items

# User input
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

# Find the maximum value and the items included in the knapsack
max_value, items = knapsack(weights, values, capacity)

items.sort()
print(f"Maximum value: {max_value}")
print("Items included (1-indexed):", items)
