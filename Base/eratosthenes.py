import math
import sys

num = int(sys.stdin.readline())
arr = [True] * (num + 1)
arr[0], arr[1] = False, False

for i in range(2, int(math.sqrt(num)) + 1):
    if arr[i] == True:
        for j in range(i * i, num + 1, i):
            arr[j] = False

for i in range(2, num + 1):
    if arr[i] == True:
        print(i, end=' ')