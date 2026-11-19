# Intro :
# You are given a 2D integer array grid of size m * n.
# You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
# At each step, you may move either right or down.
# The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.
# Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

# Example 1:
grid = [[1,2],[3,4]]
# Output: 6
# Explanation:
# There are two valid paths:
# (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
# (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
# The minimum XOR value among all valid paths is 6.

# Example 2:
# grid = [[6,7],[5,8]]
# Output: 9
# Explanation:
# There are two valid paths:
# (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
# (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
# The minimum XOR value among all valid paths is 9.

# Example 3:
# grid = [[2,7,5]]
grid = [[26,24,3],[2,22,17]]
# Output: 0
# Explanation:
# There is only one valid path:
# (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
# The XOR value of this path is 0, which is the minimum possible.

# path = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
# path[0][0] = grid[0][0]
# print(path)
def min_xor_path(grid):
    m, n = len(grid), len(grid[0])
    best = float('inf')

    def dfs(i, j, x):
        nonlocal best
        if i == m - 1 and j == n - 1:
            best = min(best, x)
            return
        if i + 1 < m:
            dfs(i + 1, j, x ^ grid[i+1][j])
        if j + 1 < n:
            dfs(i, j + 1, x ^ grid[i][j+1])

    dfs(0, 0, grid[0][0])
    return best

print(min_xor_path(grid))