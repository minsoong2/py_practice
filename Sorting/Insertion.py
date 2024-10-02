# 처리되지 않은 데이터를 적절한 위치에 삽입 O(n^2), 최선 O(N)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(0, i):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)