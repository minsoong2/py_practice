import sys

def bellman_ford(start_node):
    dist[start_node] = 0

    for i in range(n):
        for j in range(e):
            current = edge_list[j][0]
            next = edge_list[j][1]
            cost = edge_list[j][2]

            if dist[current] != inf and dist[next] > dist[current] + cost:
                dist[next] = dist[current] + cost
                if i == n - 1:
                    return True

    return False

n, e = map(int, sys.stdin.readline().split())
edge_list = []
inf = int(1e9)
dist = [inf] * (n + 1)

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edge_list.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n + 1):
        if dist[i] == inf:
            print('-1')
        else:
            print(dist[i])