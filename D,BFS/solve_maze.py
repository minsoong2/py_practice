import sys

m, n = map(int, sys.stdin.readline().split())

g = []
for l in range(m):
    g.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i]
            if 0 <= move_x < m and 0 <= move_y < n:
                if g[move_x][move_y] == 1:
                    g[move_x][move_y] = g[x][y] + 1
                    q.append((move_x, move_y))
                else:
                    continue
            else:
                continue

    print(g[m - 1][n - 1])

bfs(0, 0)