from collections import deque
import sys

n, e = map(int, sys.stdin.readline().split())
in_degree = [0] * (n + 1)
g = [[] for i in range(n + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    # DAG
    g[a].append(b)
    in_degree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in g[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()