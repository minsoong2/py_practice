import sys

inf = int(1e9)
node, edge = map(int, sys.stdin.readline().split())
g = [[inf] * (node + 1) for i in range(node + 1)]

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if a == b:
            g[a][b] = 0

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    g[a][b] = 1
    g[b][a] = 1

x, k = map(int, sys.stdin.readline().split())

for i in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            g[a][b] = min(g[a][b], g[a][i] + g[i][b])

if (g[1][k] + g[k][x]) >= inf:
    print("-1")
else: print(g[1][k] + g[k][x])