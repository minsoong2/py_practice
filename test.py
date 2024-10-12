
def bs(arr, t, start, end):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            start = mid + 1
        else:
            end = mid -1

    return -1

print(bs([0,1,2,3,4,5,6,7,8,9], 5, 0, 10))