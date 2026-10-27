# Intro
# You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
# The total value of an island is the sum of the values of all cells in the island.
# Return the number of islands with a total value divisible by k.
grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
k = 5
# Output: 2
# Explanation:
# The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.
checked = {}

def dfs1(a, i, j):
    q = []
    head = 0
    total = 0

    if 0 <= i-1 < len(a) and 0 <= j < len(a[0]) and not ((i-1, j) in checked) and a[i-1][j] != 0:
        checked[(i-1, j)] = True
        q.append((i-1, j))

    if 0 <= i+1 < len(a) and 0 <= j < len(a[0]) and not ((i+1, j) in checked) and a[i+1][j] != 0:
        checked[(i+1, j)] = True
        q.append((i+1, j))

    if 0 <= i < len(a) and 0 <= j-1 < len(a[0]) and not ((i, j-1) in checked) and a[i][j-1] != 0:
        checked[(i, j-1)] = True
        q.append((i, j-1))

    if 0 <= i < len(a) and 0 <= j+1 < len(a[0]) and not ((i, j+1) in checked) and a[i][j+1] != 0:
        checked[(i, j+1)] = True
        q.append((i, j+1))

    while head < len(q):
        x, y = q[head]
        head += 1
        total += a[x][y]

        if 0 <= x-1 < len(a) and 0 <= y < len(a[0]) and not ((x-1, y) in checked) and a[x-1][y] != 0:
            checked[(x-1, y)] = True
            q.append((x-1, y))

        if 0 <= x+1 < len(a) and 0 <= y < len(a[0]) and not ((x+1, y) in checked) and a[x+1][y] != 0:
            checked[(x+1, y)] = True
            q.append((x+1, y))

        if 0 <= x < len(a) and 0 <= y-1 < len(a[0]) and not ((x, y-1) in checked) and a[x][y-1] != 0:
            checked[(x, y-1)] = True
            q.append((x, y-1))

        if 0 <= x < len(a) and 0 <= y+1 < len(a[0]) and not ((x, y+1) in checked) and a[x][y+1] != 0:
            checked[(x, y+1)] = True
            q.append((x, y+1))

    return total


def dfs0(a, i, j):
    q = []
    head = 0
    total = 0

    if 0 <= i-1 < len(a) and 0 <= j < len(a[0]) and not ((i-1, j) in checked) and a[i-1][j] == 0:
        checked[(i-1, j)] = True
        q.append((i-1, j))

    if 0 <= i+1 < len(a) and 0 <= j < len(a[0]) and not ((i+1, j) in checked) and a[i+1][j] == 0:
        checked[(i+1, j)] = True
        q.append((i+1, j))

    if 0 <= i < len(a) and 0 <= j-1 < len(a[0]) and not ((i, j-1) in checked) and a[i][j-1] == 0:
        checked[(i, j-1)] = True
        q.append((i, j-1))

    if 0 <= i < len(a) and 0 <= j+1 < len(a[0]) and not ((i, j+1) in checked) and a[i][j+1] == 0:
        checked[(i, j+1)] = True
        q.append((i, j+1))

    while head < len(q):
        x, y = q[head]
        head += 1
        total += a[x][y]

        if 0 <= x-1 < len(a) and 0 <= y < len(a[0]) and not ((x-1, y) in checked) and a[x-1][y] == 0:
            checked[(x-1, y)] = True
            q.append((x-1, y))

        if 0 <= x+1 < len(a) and 0 <= y < len(a[0]) and not ((x+1, y) in checked) and a[x+1][y] == 0:
            checked[(x+1, y)] = True
            q.append((x+1, y))

        if 0 <= x < len(a) and 0 <= y-1 < len(a[0]) and not ((x, y-1) in checked) and a[x][y-1] == 0:
            checked[(x, y-1)] = True
            q.append((x, y-1))

        if 0 <= x < len(a) and 0 <= y+1 < len(a[0]) and not ((x, y+1) in checked) and a[x][y+1] == 0:
            checked[(x, y+1)] = True
            q.append((x, y+1))

    return total

i = 0
j = 0
lis = []
while i < len(grid) and j < len(grid[0]):
    if not (i,j) in checked:
        checked[(i,j)] = True
        print(i , j , grid[i][j] , checked)
        if grid[i][j] == 0:
            lis += [grid[i][j] + dfs0(grid , i , j)]
        else:
            lis += [grid[i][j] + dfs1(grid , i , j)]
    i += 1
    if i == len(grid):
        i = 0
        j += 1

print(lis)

res = 0
for i in lis:

    if i != 0 and i % k == 0:
        res += 1
print(res)