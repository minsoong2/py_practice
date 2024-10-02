import sys

m, n = map(int, sys.stdin.readline().split())

g = []
for i in range(m):
    g.append(list(map(int, sys.stdin.readline().strip())))

def dfs(x, y):

    if 0 <= x < m and 0 <= y < n:
        if g[x][y] == 0:
            g[x][y] = 1
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)
            return True
    else:
        return False

cnt = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            cnt += 1

print(cnt)