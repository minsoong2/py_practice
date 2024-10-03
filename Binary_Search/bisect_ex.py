from bisect import bisect_left, bisect_right
# bisect_left: 정렬된 순서를 유지, 배열 a에 x를 삽입할 가장 왼쪽 idx 반환
# bisect_right: 정렬된 순서를 유지, 배열 a애 x를 삽입할 가장 오른쪽 idx 반환

def cnt_by_range(arr, left, right):
    left_idx = bisect_left(arr, left)
    print(left_idx)
    right_idx = bisect_right(arr, right)
    print(right_idx)
    return right_idx - left_idx

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(cnt_by_range(a, 4, 4))