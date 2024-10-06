import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
l, r = map(int, sys.stdin.readline().split())

for i in range(1, n):
    arr[i] += arr[i - 1]

print(arr[r - 1] - arr[l - 2])