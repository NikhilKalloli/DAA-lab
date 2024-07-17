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

def nQueens(arr, n, col, solutions):
    if col >= n:
        solutions.append([row.copy() for row in arr])
        return


    for row in range(n):
        if isSafe(arr, row, col, n):
            arr[row][col] = 1
            nQueens(arr, n, col + 1, solutions)
            arr[row][col] = 0  

n = 4
arr = [[0] * n for _ in range(n)]
solutions = []
nQueens(arr, n, 0, solutions)
print(f"total solutions for {n}-Queens problem: {len(solutions)}\n")
for solution in solutions:
    for row in solution:
        print(row)
    print()