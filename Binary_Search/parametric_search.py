

import sys

n, cm = map(int, sys.stdin.readline().split())
cm_list = list(map(int, sys.stdin.readline().split()))

def get_cm(arr, target, start, end):

    while start <= end:
        rice_cake_len = 0
        mid = (start + end) // 2
        for i in arr:
            if i >= mid:
                rice_cake_len += i - mid
            else:
                continue

        if rice_cake_len == target:
            return mid
        elif rice_cake_len < target:
            end = mid - 1
        else:
            start = mid + 1

    return None


result = get_cm(cm_list, cm, min(cm_list), max(cm_list))
print(result)