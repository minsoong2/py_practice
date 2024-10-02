# list로 구현 가능하지만 시간복잡도 고려 deque 사용
from collections import deque

q = deque()

q.append(5)
q.append(2)
q.append(3)
q.append(7)
q.popleft()
q.append(1)
q.append(4)
q.popleft()

print(q)
q.reverse()
print(q)