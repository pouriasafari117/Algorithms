# Intro
# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.
# Example 1:
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# The grid contains four islands of 0s.
# The island spanning rows 1 to 3 and columns 1 to 4 is surrounded entirely by 1s. It also encloses the water cell at row 2, column 2. It is therefore closed.
# The single 0 at row 3, column 6 has 1s on all four sides, so it is also closed.
# The two remaining islands both lie in column 7, which is on the border of the grid, so neither of them is closed.
# Two islands are closed, shown in gray, so the answer is 2.

checked = {}

from collections import deque

class Q:
    def __init__(self):
        self.lis = deque()
    def nq(self, a):
        self.lis.append(a)
    def dq(self):
        return self.lis.popleft()
    def is_empty(self):
        return len(self.lis) == 0

def bfs(a):
    stat = True
    while not qu.is_empty():
        now = qu.dq()
        i = now[0]
        j = now[1]

        if now[0] == 0 or now[0] == len(a)-1 or now[1] == 0 or now[1] == len(a[0])-1:
            stat = False

        if 0 <= i-1 < len(a) and 0 <= j < len(a[0]) and not ((i-1, j) in checked) and a[i-1][j] == 0:
            checked[(i-1, j)] = True
            qu.nq((i-1, j))

        if 0 <= i+1 < len(a) and 0 <= j < len(a[0]) and not ((i+1, j) in checked) and a[i+1][j] == 0:
            checked[(i+1, j)] = True
            qu.nq((i+1, j))

        if 0 <= i < len(a) and 0 <= j-1 < len(a[0]) and not ((i, j-1) in checked) and a[i][j-1] == 0:
            checked[(i, j-1)] = True
            qu.nq((i, j-1))

        if 0 <= i < len(a) and 0 <= j+1 < len(a[0]) and not ((i, j+1) in checked) and a[i][j+1] == 0:
            checked[(i, j+1)] = True
            qu.nq((i, j+1))
    return stat

res = 0
qu = Q()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0 and not (i , j) in checked:
            # print(i , j)
            qu.nq((i , j))
            if bfs(grid):
                # print(' salam')
                res += 1
print(res)