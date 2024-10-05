import sys

inf = int(1e9)

node, edge = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
g = [[] for i in range(node + 1)]
visited = [False] * (node + 1)
distance = [inf] * (node + 1)

for _ in range(edge):
    # a 노드에서 b 노드까지 가는 비용이 c
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))

# 방문하지 않는 노드, 가장 최단 거리가 짧은 노드 idx 반환
def get_smallest_node():
    min_value = inf
    idx = 0

    for i in range(1, node + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i

    return idx

def dijkstra(start_node):
    distance[start_node] = 0
    visited[start_node] = True

    # start node로 부터 바로 도달이 가능한 node들의 거리 update
    for i in g[start_node]:
        distance[i[0]] = i[1]

    for i in range(node - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in g[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, node + 1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])