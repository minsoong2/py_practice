import sys
from collections import deque

def bfs(x, y):

    q = deque()
    q.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < r and 0 <= my < c:
                if g[mx][my] == 1:
                    g[mx][my] = g[x][y] + 1
                    q.append((mx, my))
                else:
                    continue
            else:
                continue

r, c = map(int, sys.stdin.readline().split())
g = []
for _ in range(r):
    g.append(list(map(int, sys.stdin.readline().strip())))

bfs(0, 0)
print(g[r-1][c-1])