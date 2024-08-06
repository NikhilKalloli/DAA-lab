# O(n * W)
def knapsack_recursive(ind, W, weights, values, dp):
    if ind == 0:
        if weights[0] <= W:
            return values[0]
        return 0

    if dp[ind][W] != -1:
        return dp[ind][W]

    not_take = knapsack_recursive(ind - 1, W, weights, values, dp)
    take = float('-inf')
    if weights[ind] <= W:
        take = values[ind] + knapsack_recursive(ind - 1, W - weights[ind], weights, values, dp)

    dp[ind][W] = max(take, not_take)
    return dp[ind][W]

def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [[-1 for _ in range(max_weight + 1)] for _ in range(n)]
    return knapsack_recursive(n - 1, max_weight, weights, values, dp)


weights = [1, 2, 3, 2, 4, 5, 6, 7]
values = [1, 2, 3, 4, 5, 8, 13, 21]
max_weight = 10

print(f"Maximum value for the knapsack problem is: {knapsack(weights, values, max_weight)}")