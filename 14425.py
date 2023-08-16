import sys
from collections import Counter
a, b = map(int, sys.stdin.readline().split())
standard = []
check = []

for i in range(a):
    standard.append(sys.stdin.readline())
for i in range(a, a+b):
    check.append(sys.stdin.readline())

counter = Counter(standard)
cnt = 0
for i in check:
    if counter[i] == 1:
        cnt += 1
    else:
        continue
print(cnt)