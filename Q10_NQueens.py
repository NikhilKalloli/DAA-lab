def isSafe(arr, row, col, n):
    for i in range(col):
        if arr[row][i]:
            return False
    
    i, j = row, col
    while i >= 0 and j >= 0:
        if arr[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if arr[i][j]:
            return False
        i += 1
        j -= 1

    return True

def nQueens(arr, n, column, solutions):
    if column >= n:
        solutions.append(["".join(['Q' if arr[i][j] else '.' for j in range(n)]) for i in range(n)])
        return

    for i in range(n):
        if isSafe(arr, i, column, n):
            arr[i][column] = 1
            nQueens(arr, n, column + 1, solutions)
            arr[i][column] = 0  # Backtrack

n = 4
arr = [[0] * n for _ in range(n)]
solutions = []
nQueens(arr, n, 0, solutions)
print(f"total solutions for {n}-Queens problem: {len(solutions)}\n")
for solution in solutions:
    for row in solution:
        print(row)
    print()