import sys

num = int(sys.stdin.readline())
l = []
for i in range(num):
    a = int(sys.stdin.readline())
    if a == 0:
        l.pop()
    else:
        l.append(a)
print(sum(l))