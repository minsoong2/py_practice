import sys

n, k = map(int, sys.stdin.readline().split())

arr_a = list(map(int, sys.stdin.readline().split()))
arr_b = list(map(int, sys.stdin.readline().split()))

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(k):
    arr_a[i], arr_b[i] = arr_b[i], arr_a[i]

print(sum(arr_a))