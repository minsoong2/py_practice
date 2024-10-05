import sys

inf = int(1e9)
node, edge = map(int, sys.stdin.readline().split())
g = [[inf] * (node + 1) for i in range(node + 1)]

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if a == b:
            g[a][b] = 0

for _ in range(edge):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a][b] = c

for i in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            g[a][b] = min(g[a][b], g[a][i] + g[i][b])

for a in range(1, node + 1):
    for b in range(1, node + 1):
        if g[a][b] == inf:
            print("INF")
        else:
            print(g[a][b], end= ' ')
    print()