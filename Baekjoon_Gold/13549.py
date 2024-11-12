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

        for x in (node * 2, node + 1, node -1):
            if x < 0 or x > 100000:
                continue

            cost = dist
            if x != node * 2:
                cost = dist + 1

            if cost < distance[x]:
                distance[x] = cost
                heapq.heappush(q, (cost, x))

n, k = map(int, sys.stdin.readline().split())
inf = 1e9
distance = [inf] * 100001
dijkstra(n)
print(distance[k])