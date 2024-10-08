import sys

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_parent_path_compression(parent, x):
    if parent[x] != x:
        # Path Compression
        parent[x] = find_parent_path_compression(parent, parent[x])
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

for i in range(1, node + 1):
    parent[i] = i

for i in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)

print('Sets: ', end='')
for i in range(1, node + 1):
    print(find_parent(parent, i), end=' ')

print()

print('Parent table: ', end='')
for i in range(1, node + 1):
    print(parent[i], end=' ')