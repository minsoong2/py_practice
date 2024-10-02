# 작은 값 < Pivot < 큰 값
# Divide and Conquer O(NlogN)
# 최악 O(N^2) - 0(pivot) 1 2 3 4 5 6 7 8 9

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    l = [x for x in tail if x <= pivot]
    r = [x for x in tail if x > pivot]

    return quick_sort2(l) + [pivot] + quick_sort2(r)

quick_sort(arr, 0, len(arr)-1)
print(arr)
print(quick_sort2(arr2))