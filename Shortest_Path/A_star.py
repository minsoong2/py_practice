import heapq

# A* 알고리즘에서 사용할 노드 클래스
class Node:
    def __init__(self, position, g_cost=0, h_cost=0):
        self.position = position  # 노드의 좌표 (x, y)
        self.g = g_cost  # 시작점에서 현재 노드까지의 비용
        self.h = h_cost  # 현재 노드에서 목표 노드까지의 예상 비용 (휴리스틱)
        self.f = g_cost + h_cost  # 총 비용 f = g + h
        self.parent = None  # 경로 추적을 위해 부모 노드를 기록

    def __lt__(self, other):
        return self.f < other.f  # f값을 기준으로 우선순위 큐에서 비교


def heuristic(node_position, goal_position):
    return ((node_position[0] - goal_position[0]) ** 2 + (node_position[1] - goal_position[1]) ** 2) ** 0.5


# A* 알고리즘 구현
def a_star_algorithm(start, goal, grid):
    open_list = []  # 우선순위 큐로 사용할 리스트 (heapq 사용)
    closed_list = set()  # 방문한 노드를 기록할 집합

    start_node = Node(start, 0, heuristic(start, goal))  # 시작 노드
    heapq.heappush(open_list, start_node)

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # 경로를 역순으로 리턴

        for move in moves:
            neighbor_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            # 그리드 범위를 벗어나지 않는지 확인
            if neighbor_pos[0] < 0 or neighbor_pos[0] >= len(grid) or neighbor_pos[1] < 0 or neighbor_pos[1] >= len(grid[0]):
                continue

            # 장애물
            if grid[neighbor_pos[0]][neighbor_pos[1]] == 1:
                continue

            # 이미 방문한 노드
            if neighbor_pos in closed_list:
                continue

            g_cost = current_node.g + 1
            h_cost = heuristic(neighbor_pos, goal)
            neighbor_node = Node(neighbor_pos, g_cost, h_cost)

            heapq.heappush(open_list, neighbor_node)
            neighbor_node.parent = current_node  # 부모 노드를 설정

    return None

# 그리드 설정 (0: 이동 가능, 1: 장애물)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # 시작 위치
goal = (4, 4)  # 목표 위치

path = a_star_algorithm(start, goal, grid)

if path:
    print("찾은 경로:", path)
else:
    print("경로를 찾을 수 없습니다.")
