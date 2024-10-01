import sys
from itertools import permutations, combinations

arr = list(map(int, sys.stdin.readline().split()))
print(arr)

result_p = list(permutations(arr,3))
result_c = list(combinations(arr, 2))
print(result_p)
print(result_c)