import sys
import heapq

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def min_heap(arr):
    h = []
    re = []

    for i in range(len(arr)):
        heapq.heappush(h, arr[i])

    for i in range(len(arr)):
        re.append(heapq.heappop(h))

    print(re)

min_heap(arr)

def max_heap(arr):
    h = []
    re = []

    for i in range(len(arr)):
        heapq.heappush(h, -arr[i])

    for i in range(len(arr)):
        re.append(-heapq.heappop(h))

    print(re)

max_heap(arr)