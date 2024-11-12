import sys

n, e = map(int, sys.stdin.readline().split())
inf = 1e9
g = [[inf] * n for _ in range(n)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a-1][b-1] = c

for i in range(n):
    for a in range(n):
        for b in range(n):
            g[a][b] = min(g[a][b], g[a][i] + g[i][b])

re = []
for a in range(n):
    for b in range(n):
        if a == b:
            re.append(g[a][b])

if min(re) == inf:
    print(-1)
else:
    print(min(re))