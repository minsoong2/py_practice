import sys

a = int(sys.stdin.readline())
l = [0 for i in range(10001)] # 0 ~ 10000
for i in range(a):
    l[int(sys.stdin.readline())] += 1
for i in range(10001):
    if l[i] == 0:
        continue
    else:
        for _ in range(l[i]):
            print(i)