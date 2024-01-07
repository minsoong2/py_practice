import sys
import math

num = int(sys.stdin.readline())
l = []
for i in range(num):
    l.append(int(sys.stdin.readline()))

re = []
for i in range(len(l)):
    if i+1 == len(l):
        break
    length = l[i+1] - l[i]
    re.append(length)

gcd = math.gcd(*re)
cnt = 0
for i in range(len(l)):
    if i+1 == len(l):
        break
    if l[i+1] == l[i] + gcd:
        continue
    else:
        while True:
            l[i] = l[i] + gcd
            cnt += 1
            if l[i + 1] == l[i] + gcd:
                break
print(cnt)