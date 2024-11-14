import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    arr[i] += arr[i-1]

remain = [0] * m
for i in arr:
    remain[i % m] += 1

cnt = remain[0]
for i in remain:
    cnt += i * (i-1) // 2

print(cnt)
