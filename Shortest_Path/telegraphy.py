import sys
import heapq

inf = int(1e9)

node, edge, start = map(int, sys.stdin.readline().split())
g = [[] for i in range(node + 1)]
distance = [inf] * (node + 1)

for _ in range(edge):
    # a 노드에서 b 노드까지 가는 비용이 c
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))

def dijkstra(start):
    q = []
    # (cost, node)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 처리된 node
        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0
max_dist = 0
for d in distance:
    if d != inf:
        cnt += 1
        max_dist = max(max_dist, d)

print(cnt - 1, max_dist)