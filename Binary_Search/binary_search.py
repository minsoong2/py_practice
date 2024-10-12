import sys

def binary_search_recursive(arr, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, end)
    else:
        return binary_search_recursive(arr, target, start, mid - 1)

def binary_search_loop(arr, target, start, end):

    while start < end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

n, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = binary_search_loop(arr, target, 0, n - 1)
if result is None:
    print('No data')
else:
    print(result + 1)