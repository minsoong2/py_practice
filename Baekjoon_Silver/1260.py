import sys
from collections import deque

def dfs(g, start, visited):
    visited[start] = True
    print(start, end=' ')

    for node in g[start]:
        if not visited[node]:
            dfs(g, node, visited)

def bfs(g, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')

        for node in g[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True

n, e, start = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

for l in g:
    l.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(g, start, visited_dfs)
print()
bfs(g, start, visited_bfs)