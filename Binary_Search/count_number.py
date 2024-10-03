import sys
from bisect import bisect_left, bisect_right

n, num = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

l_idx = bisect_left(num_list, num)
r_idx = bisect_right(num_list, num)

print(r_idx - l_idx)