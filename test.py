import sys

l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    l = [x for x in tail if x <= pivot]
    r = [x for x in tail if x > pivot]

    return quick(l) + [pivot] + quick(r)

print(quick(arr))