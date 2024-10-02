def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for idx in graph[v]:
            if not visited[idx]:
                queue.append(idx)
                visited[idx] = True


g = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

dfs_visited = [False] * 9
bfs_visited = [False] * 9

dfs(g, 1, dfs_visited)
print()
bfs(g, 1, bfs_visited)