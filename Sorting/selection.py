# 가장 작은 값을 골라 맨 앞에 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    num = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = num

    print(arr)