import sys

n = int(sys.stdin.readline())
parent = [0] * (n + 1)
d = [0] * (n + 1)
c = [0] * (n + 1)
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

def dfs(x, depth):
    c[x] = True
    d[x] = depth

    for y in g[x]:
        if c[x]:
            continue
        parent[y] = x
        dfs(x, depth + 1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

dfs(1, 0)

couple = int(sys.stdin.readline())
for _ in range(couple):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))