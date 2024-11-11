import sys
import heapq

inf = 1e9

def dijkstra(start):
    distance = [inf] * (n + 1)
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

    return distance

n, e = map(int, sys.stdin.readline().split())
g = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())
dist_start = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

min_cost = min(dist_start[v1] + dist_v1[v2] + dist_v2[n],
               dist_start[v2] + dist_v2[v1] + dist_v1[n])

if min_cost >= inf:
    print(-1)
else:
    print(min_cost)