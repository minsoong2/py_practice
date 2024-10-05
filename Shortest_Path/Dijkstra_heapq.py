import sys, heapq

inf = int(1e9)

node, edge = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
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

for i in range(1, node + 1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])