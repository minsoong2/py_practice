import sys

a, b = map(int, sys.stdin.readline().split())
arr = []
for i in range(a, b+1):
    cnt = 0
    if i == 0 or i == 1 or i == 2:
        arr.append(2)
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            arr.append(i)

l = list(set(arr))
for i in l:
    print(i)