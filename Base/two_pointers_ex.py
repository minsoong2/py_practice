import sys

size, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
interval_sum, end = 0, 0
# start 고정, end 위치 이동
for i in range(size):
    while interval_sum < s and end < size:
        interval_sum += arr[end]
        end += 1
    if interval_sum == s:
        cnt += 1
    interval_sum -= arr[i]

print(cnt)