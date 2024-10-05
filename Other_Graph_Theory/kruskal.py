import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

node, edge = map(int, sys.stdin.readline().split())
parent = [0] * (node + 1)
edge_list = []
result = 0

for i in range(1, node + 1):
    parent[i] = i

for _ in range(edge):
    a, b, cost = map(int, sys.stdin.readline().split())
    edge_list.append((cost, a, b))

edge_list.sort()

for e in edge_list:
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)