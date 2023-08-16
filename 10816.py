import sys
from collections import Counter

n_1 = int(sys.stdin.readline())
l_1 = list(map(int, sys.stdin.readline().split()))

n_2 = int(sys.stdin.readline())
l_2 = list(map(int, sys.stdin.readline().split()))

counter_l_1 = Counter(l_1)
for i in l_2:
    if counter_l_1[i]:
        print(counter_l_1[i], end=' ')
    else:
        print(0, end=' ')