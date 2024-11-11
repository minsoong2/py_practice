import sys
import heapq

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for bc in g[node]:
            cost = dist + bc[1]
            if cost < distance[bc[0]]:
                distance[bc[0]] = cost
                heapq.heappush(q, (cost, bc[0]))

n, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
g = [[] for _ in range(n + 1)]
inf = 1e9
distance = [inf] * (n + 1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])