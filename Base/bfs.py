from collections import deque


def deque_bfs(g, start):

    pre_visit = []
    need_visit = deque([start])

    while need_visit:
        node = need_visit[0]
        del need_visit[0]

        if node not in pre_visit:
            pre_visit.append(node)
            need_visit.extend(g[node])

    return pre_visit


graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


print(deque_bfs(graph, 'A'))